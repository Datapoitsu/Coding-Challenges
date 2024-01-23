def top_note(student):
	return {"name":student["name"],"top_note":max(student["notes"])}