
def normalize_skills(skills):
    """Remove extra spaces, blank values, and duplicate skills."""
    normalized = []
    seen_keys = []

    for skill in skills:
        readable_skill = str(skill).strip()

        if readable_skill == "":
            continue

        comparison_key = readable_skill.lower()

        if comparison_key not in seen_keys:
            seen_keys.append(comparison_key)
            normalized.append(readable_skill)

    return normalized


class StudentProfile:
    def __init__(self, name, skills):
        self._student_name = str(name).strip()
        self._student_skills = normalize_skills(skills)

    def get_name(self):
        return self._student_name

    def get_skills(self):
        return self._student_skills.copy()


class JobDescription:
    def __init__(self, title, required_skills):
        self._job_title = str(title).strip()
        self._required_skills = normalize_skills(required_skills)

    def get_title(self):
        return self._job_title

    def get_required_skills(self):
        return self._required_skills.copy()