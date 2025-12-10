

from dataclasses import dataclass


@dataclass(frozen=True)
class JobPeriod:
    role: str
    company: str
    start_year: int
    start_month: int
    end_year: int
    end_month: int


def linkedin_buggy_duration(start_y, start_m, end_y, end_m):
    """
    LinkedIn's inferred internal logic:
    Adds +1 month even when start and end month are identical.
    """
    return (end_y - start_y) * 12 + (end_m - start_m) + 1


def correct_duration(start_y, start_m, end_y, end_m):
    """
    Correct elapsed duration (industry-standard):
    No inclusive counting. Real number of full months passed.
    """
    return (end_y - start_y) * 12 + (end_m - start_m)


def pretty_format(months):
    """Convert months → (years, months)."""
    years = months // 12
    months = months % 12
    return f"{years} yrs {months} mos"



test_jobs = [
    JobPeriod(
        role="Lead Engineer",
        company="HCL Technologies",
        start_year=2021, start_month=2,
        end_year=2023, end_month=2,
    ),
    JobPeriod(
        role="Team Lead",
        company="IMSI India Pvt. Ltd.",
        start_year=2017, start_month=11,
        end_year=2021, end_month=1,
    ),
    JobPeriod(
        role="Senior Machine Learning Developer",
        company="Zimro Private Limited",
        start_year=2018, start_month=11,
        end_year=2021, end_month=10,
    )
]



for job in test_jobs:
    buggy = linkedin_buggy_duration(job.start_year, job.start_month, job.end_year, job.end_month)
    correct = correct_duration(job.start_year, job.start_month, job.end_year, job.end_month)

    print(f"\n=== {job.role} @ {job.company} ===")
    print(f"Start: {job.start_month}/{job.start_year}  End: {job.end_month}/{job.end_year}")
    print(f"LinkedIn shows (buggy):     {pretty_format(buggy)}")
    print(f"Correct calculation:         {pretty_format(correct)}")

    if buggy != correct:
        print("⚠ ERROR DETECTED: LinkedIn is adding an extra month.")
    else:
        print("✔ No error for this job.")
