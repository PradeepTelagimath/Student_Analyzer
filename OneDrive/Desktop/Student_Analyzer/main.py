
from models import StudentProfile, JobDescription
from analyzers import MatchScoreCalculator, MissingSkillDetector
from manager import Manager


def run_analysis(student, job):
    analyzers = [
        MatchScoreCalculator(),
        MissingSkillDetector()
    ]

    manager = Manager(student, job, analyzers)
    manager.display_report()


def run_edge_case_tests():
    print("\n\nEDGE-CASE CHECKS")

    # Test 1: Job has no required skills.
    student = StudentProfile("Test Student", ["Python", "SQL"])
    empty_job = JobDescription("Empty Requirements Job", [])

    results = Manager(
        student,
        empty_job,
        [MatchScoreCalculator(), MissingSkillDetector()]
    ).generate_report()

    assert results["match_percentage"] == 0.0
    assert results["missing_skills"] == []

    # Test 2: Student has no skills.
    empty_student = StudentProfile("No Skills", [])
    job = JobDescription("Python Developer", ["Python", "SQL"])

    results = Manager(
        empty_student,
        job,
        [MatchScoreCalculator(), MissingSkillDetector()]
    ).generate_report()

    assert results["match_percentage"] == 0.0
    assert results["missing_skills"] == ["Python", "SQL"]

    # Test 3: Duplicate and differently capitalized skills.
    duplicate_student = StudentProfile(
        "Gamana", [" Python ", "python", "SQL", "sql"]
    )

    duplicate_job = JobDescription(
        "Python Developer", ["Python", "SQL", "SQL"]
    )

    results = Manager(
        duplicate_student,
        duplicate_job,
        [MatchScoreCalculator(), MissingSkillDetector()]
    ).generate_report()

    assert results["match_percentage"] == 100.0
    assert results["matching_skills"] == ["Python", "SQL"]

    print("All edge-case checks passed.")


def main():
    # Create the student profile.
    student = StudentProfile(
        "Gamana",
        ["Python", " SQL "]
    )

    # First job description.
    python_job = JobDescription(
        "Python Developer",
        ["Python", "SQL", "Django", "REST API", "Git"]
    )

    run_analysis(student, python_job)

    # Second job description for the same student.
    full_stack_job = JobDescription(
        "Junior Full Stack Developer",
        ["Python", "JavaScript", "React", "SQL"]
    )

    run_analysis(student, full_stack_job)

    # Run automatic checks.
    run_edge_case_tests()


if __name__ == "__main__":
    main()