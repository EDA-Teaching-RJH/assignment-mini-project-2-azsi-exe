**REFLECTION DOCUMENT**
MotoLog, an project that incorporates learning within lectures, and self learning beyond, tied with my passion, is a system that allows bikers to manage the bikes data, including adding, deleting, updating, and analysing service records with the use of CSV files.

**TECHNICAL REQUIREMENTS**
I used CSV file handling to store and retrieve motorbikes and service record data. This links directly to lecture content on file operations I/O, including reading and writing structured data. The add_bike, view_all_bikes, and update_mileage functions aim to demonstrate this.

Regex (Regular Expressions) was used to validate the users input. For example:
	•	Registration format: AB12 CDE
	•	Date format: DD/MM/YYYY
This ensures that the users inputs follows a correct structure consistently, which was taught in the validation lectures.

I implemented OOP using two classes:
	•	Vehicle (The Parent Class)
	•	Motorbike (The Child Class)
The Motorbike class inherits attributes from Vehicle and adds the mileage. This demonstrates inheritance and code reuse, which were key concepts covered in lectures.

I used pytest to test core functions, including adding a bike, updating mileage, and deleting a bike. Assertions were used to verify expected outcomes. This reflects on the workshop on testing and validation.

I used built-in Python libraries such as CSV for file handling, statistics for calculating average service costs and the re for regex validation. This demonstrates the use of external modules to extend the functionality of the code.

I extended the project by adding:
	•	Service logging system
	•	Service analytics (total services and average cost)
This goes beyond the basic requirements of the project, and shows independent development, beyonf just the lectures.

**CHALLENGES**
One challenge I faced while building this code was ensuring that test cases worked correctly with the existing data in the CSV file. Initially, I checked only the last row of the file, which caused a test error. I solved this by looping through all records to confirm the existence of a bike, instead of just the last row. Another challenge was structuring the program using OOP. I did this by separating shared attributes into a parent class, and the extending functionality in a child class.

**DEVELOPING PROCESS**
The project was developed incrementally, with features added step by step, testing within VS code and structuring and planning in my notebook. I used Git to track progress and document changes through important commits.

**CONCLUSION**
This project allowed me to apply theoretical concepts in a practical way, with a topic I am passionate in. I improved my understanding of python, specifically in file handling, validation, OOP, and testing, and developed a structured program I hope to develop more in the future.