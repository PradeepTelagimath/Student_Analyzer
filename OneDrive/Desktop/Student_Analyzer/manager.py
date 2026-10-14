
class Manager:
    def __init__(self, student, job, analyzers):
        self._student = student
        self._job = job
        self._analyzers = analyzers

    def generate_report(self):
        results = {}

        for analyzer in self._analyzers:
            analyzer_result = analyzer.analyze(
                self._student, self._job
            )
            results.update(analyzer_result)

        return results

    def display_report(self):
        results = self.generate_report()

        required_count = results["required_count"]
        matching_count = results["matching_count"]
        percentage = results["match_percentage"]

        print("\nSTUDENT-JOB SKILL ANALYSIS REPORT\n")

        print(f"Student Name: {self._student.get_name()}")
        print(f"Job Title: {self._job.get_title()}")
        print(f"Required Skills: {required_count}")

        print("\nMatching Skills:")
        if results["matching_skills"]:
            for skill in results["matching_skills"]:
                print(f"- {skill}")
        else:
            print("- None")

        print("\nMissing Skills:")
        if results["missing_skills"]:
            for skill in results["missing_skills"]:
                print(f"- {skill}")
        else:
            print("- None")

        print(f"\nMatch Score: {percentage:.0f}%")

        print("\nExplanation:")
        print(
            f"The student matches {matching_count} out of "
            f"{required_count} unique required skills. "
            f"Therefore, the skill match percentage is "
            f"{percentage:.0f}%."
        )