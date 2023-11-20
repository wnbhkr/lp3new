// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        string name;
        uint8 age;
        string major;
    }

    Student[] public students;

    event StudentAdded(string name, uint8 age, string major);

    function addStudent(string memory _name, uint8 _age, string memory _major) public {
        Student memory newStudent = Student(_name, _age, _major);
        students.push(newStudent);
        emit StudentAdded(_name, _age, _major);
    }

    function getStudent(uint256 index) public view returns (string memory, uint8, string memory) {
        require(index-1 < students.length, "Student index out of bounds");
        Student storage student = students[index-1];
        return (student.name, student.age, student.major);
    }

    function getNumberOfStudents() public view returns (uint256) {
        return students.length;
    }

    fallback() external {
        revert("Fallback function: This contract does not accept Ether.");
    }
}