// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Program: Student Data Smart Contract
// Aim: To create and store student information using structures and arrays,
// and demonstrate the use of a fallback function in Solidity.

// --- Contract Declaration ---
contract StudentData {

    // Step 1: Structure Declaration
    // Logic: A structure groups related data items together (like a record)
    struct Student {
        uint256 id;             // Unique student ID
        string name;            // Student's name
        uint8 age;              // Student's age
        string course;          // Course enrolled
    }

    // Step 2: Array to store multiple students
    // Logic: Dynamic array allows adding any number of students
    Student[] public students;

    // Step 3: Function to add a new student
    function addStudent(uint256 _id, string memory _name, uint8 _age, string memory _course) public {
        // Create a new Student struct and add to the array
        Student memory newStudent = Student({
            id: _id,
            name: _name,
            age: _age,
            course: _course
        });

        students.push(newStudent);   // Add new student to the array
    }

    // Step 4: Function to get student details by ID
    function getStudent(uint256 _index) public view returns (uint256, string memory, uint8, string memory) {
        require(_index < students.length, "Invalid index.");
        Student memory s = students[_index];   // Fetch student at given index
        return (s.id, s.name, s.age, s.course);
    }

    // Step 5: Fallback Function
    // Logic: Executes automatically when someone sends Ether or calls a non-existing function.
    fallback() external payable {
        // You can use this to log or accept Ether
    }

    // Step 6: Receive Function (to receive Ether)
    // Logic: Executes when contract receives Ether without data
    receive() external payable {}

    // Step 7: Function to check contract's Ether balance (for observation)
    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
