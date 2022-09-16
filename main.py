import create_course
import course_params


difficulty = input("choose difficulty: Easy, Medium Hard")

hole1 = create_course.Hole(course_params.length,course_params.sand,course_params.water,course_params.width,difficulty)

hole1.create_hole()

print (f"w:  {hole1.width_marker}")
for x in range(len(hole1.map)):
  letter = ["A","B","C","D","E","F","G","H","I","J","K","L"]
  print (f"{letter[x]}: {hole1.map[x]}")