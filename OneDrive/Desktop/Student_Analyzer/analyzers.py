
from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    @abstractmethod
    def analyze(self, student, job):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self, student, job):
        student_skills = student.get_skills()
        required_skills = job.get_required_skills()

        matching_skills = []

        for required_skill in required_skills:
            for student_skill in student_skills:
                if required_skill.lower() == student_skill.lower():
                    matching_skills.append(required_skill)
                    break

        required_count = len(required_skills)
        matching_count = len(matching_skills)

        if required_count == 0:
            percentage = 0.0
        else:
            percentage = (
                matching_count / required_count
            ) * 100

        return {
            "matching_skills": matching_skills,
            "matching_count": matching_count,
            "required_count": required_count,
            "match_percentage": percentage
        }


class MissingSkillDetector(SkillAnalyzer):
    def analyze(self, student, job):
        student_skills = student.get_skills()
        required_skills = job.get_required_skills()

        missing_skills = []

        for required_skill in required_skills:
            found = False

            for student_skill in student_skills:
                if required_skill.lower() == student_skill.lower():
                    found = True
                    break

            if not found:
                missing_skills.append(required_skill)

        return {"missing_skills": missing_skills}