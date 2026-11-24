#!/usr/bin/env python3
"""Mechanical checks for a drafted email. Catches what regex can catch; the
specificity test and the voice still need a human-style read.

Usage:
  python3 lint_email.py draft.txt            # or pipe the draft on stdin
  python3 lint_email.py --max-chars 300 note.txt   # LinkedIn connection note
  python3 lint_email.py --selftest

Put the subject on the first line as "Subject: ..." if there is one.
Exit code 1 when anything is flagged.
"""
import re
import sys

PHRASES = [
    # chatbot residue and stock openers/closers
    "hope this email finds you", "hope this finds you", "i hope you're doing well",
    "i hope you are doing well", "hope you're well", "hope all is well",
    "hope things have been", "i'm reaching out", "i am reaching out",
    "i wanted to reach out", "i wanted to express", "sincere gratitude",
    "don't hesitate to", "do not hesitate to", "let me know if you'd like",
    "happy to help", "i hope this helps", "just checking in", "bumping this",
    "circling back", "circle back", "did you see my last", "i never heard back",
    "as of my last", "quick question", "touch base",
    # warm-up openers: delay the point
    "thought i'd reach out", "thought i would reach out", "my name is",
    "i'm writing to", "i am writing to", "allow me to introduce", "i came across your",
    "i've been following your", "hope you had a great", "hope you're having a great",
    "hope your week", "i know you're busy", "i know you are busy",
    # internal and client-issue boilerplate
    "per my last email", "as previously stated", "not sure if you saw my last",
    "apologize for any inconvenience", "sorry for any inconvenience",
    "mistakes were made", "we take this very seriously", "never happen again",
    "sorry if you feel", "sorry to bother you",
    # job-email boilerplate
    "align well with", "aligns well with", "aligns with", "align with",
    "resonated", "resonates with me", "passionate about",
    "doing amazing things", "exciting time", "perfect fit", "ideal candidate",
    "i believe my skills", "close to how i", "how i like to work", "like that too",
    "mirrors my own",
    # grand significance / vague authority
    "a testament to", "pivotal moment", "evolving landscape", "at the intersection of",
    "speaks to a broader", "many teams struggle", "it's widely understood",
]
WORDS = [
    "crucial", "pivotal", "robust", "leverage", "leveraging", "delve", "underscore",
    "underscores", "showcase", "showcasing", "tapestry", "testament", "intricate",
    "meticulous", "garner", "foster", "bolster", "seamless", "seamlessly", "holistic",
    "comprehensive", "unlock", "empower", "elevate", "transformative", "game-changing",
    "synergy", "synergies", "vibrant", "thrilled", "truly", "deeply",
]
TAILS = ["highlighting", "underscoring", "emphasizing", "showcasing", "reflecting",
         "demonstrating", "signaling"]


def lint(text, max_chars=None):
    issues = []
    lines = text.strip().splitlines()
    subject = None
    if lines and lines[0].lower().startswith("subject:"):
        subject = lines[0].split(":", 1)[1].strip()
        body = "\n".join(lines[1:]).strip()
    else:
        body = "\n".join(lines).strip()
    low = body.lower()

    if body.count("—") > 1:
        issues.append(f"{body.count(chr(0x2014))} em dashes (max 1, prefer 0)")
    if re.search("[‘’“”]", body):
        issues.append("curly quotes/apostrophes (use straight ones)")
    if body.count("!") > 1:
        issues.append(f"{body.count('!')} exclamation points (roughly 1 max)")
    if re.search(r"\*\*|^#{1,6} |^---$", body, re.M):
        issues.append("markdown (bold/headers/rules) in body")
    if re.search(r"^subject:", body, re.I | re.M):
        issues.append("'Subject:' line inside the body")
    for m in re.findall(r"\[[^\]\n]{2,}\]|\bTODO\b|\bTK\b", body):
        issues.append(f"unfilled placeholder: {m}")
    for p in PHRASES:
        if p in low or (subject and p in subject.lower()):
            issues.append(f"stock phrase: '{p}'")
    for w in WORDS:
        if re.search(rf"\b{re.escape(w)}\b", low):
            issues.append(f"AI-tell word: '{w}'")
    for t in TAILS:
        if re.search(rf",\s+{t}\b", low):
            issues.append(f"participle tail: ', {t} ...'")
    if re.search(r"\bnot (just|only|about)\b[^.]{0,60}\bbut\b|\bisn't\b[^.]{0,50}, it's\b"
                 r"|, not the [a-z ]{1,40}[.!]", low):
        issues.append("'not X but Y' construction")
    starts = [s.split()[0].lower() for s in re.split(r"(?<=[.!?])\s+", body) if s.split()]
    if any(a == b == c for a, b, c in zip(starts, starts[1:], starts[2:])):
        issues.append("three sentences in a row start with the same word")
    if subject is not None:
        if len(subject.split()) > 6:
            issues.append(f"subject is {len(subject.split())} words (outreach aims 2-6; "
                          "fine for internal, client, investor subjects)")
        if subject.istitle() and len(subject.split()) > 1:
            issues.append("subject in Title Case")
    if max_chars and len(body) > max_chars:
        issues.append(f"{len(body)} chars, over the {max_chars} limit")

    words = len(body.split())
    return issues, words


def selftest():
    bad = ("Subject: Exploring Product Opportunities At Acme\n"
           "I hope this email finds you well — I'm reaching out because I'm "
           "passionate about Acme — it's not just a job, but a mission! Truly! "
           "Your work is a testament to [the specific thing from the interview that "
           "stuck with you, e.g. how she described the roadmap sequencing].")
    issues, _ = lint(bad)
    joined = " | ".join(issues)
    for needle in ["em dashes", "exclamation", "placeholder", "hope this email",
                   "passionate", "testament", "not X but Y", "Title Case"]:
        assert needle in joined, f"selftest missed: {needle}\n{joined}"
    good = ("Subject: coin collector + tech\n"
            "hey sam,\n\nSaw the raise, congrats, that's huge! I caught that you "
            "collect coins; I've been at it since I was 15.\n\n-- James")
    issues, _ = lint(good)
    assert issues == [], issues
    assert lint("x" * 301, max_chars=300)[0], "char limit not enforced"
    assert lint("Subject: quick question\nhey sam,\nok")[0], "subject phrase missed"
    assert lint("hey sam,\nThought I'd reach out about the role.")[0], "warm-up missed"
    print("selftest ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--selftest" in args:
        selftest()
        sys.exit(0)
    max_chars = None
    if "--max-chars" in args:
        i = args.index("--max-chars")
        max_chars = int(args[i + 1])
        del args[i:i + 2]
    text = open(args[0], encoding="utf-8").read() if args else sys.stdin.read()
    issues, words = lint(text, max_chars)
    print(f"{words} words, {len(text.strip())} chars")
    for i in issues:
        print(f"- {i}")
    print("clean" if not issues else f"{len(issues)} flag(s) - fix or justify each")
    sys.exit(1 if issues else 0)
