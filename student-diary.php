<?php

// Students, Grades and Attendance
$student = array(
  array('name' => 'Name', 'Grade' => 8.5, 'presence' => true),
  array('name' => 'Name', 'Grade' => 9.0, 'presence' => true),
  array('name' => 'Name', 'Grade' => 7.5, 'presence' => false),
  array('name' => 'Name', 'Grade' => 6.0, 'presence' => true),
);

// Alphabetic Order
function cmp($a, $b) {
  return strcmp($a['name'], $b['name']);
}

// Comparison
usort ($students, "cmp");

// Print on terminal
foreach ($students as $student) {
  echo "Student: " . $student['nome'] . ", Nota: " . $student['nota'] . ", Presence: " . ($student['presence'] ? 'Presence' : 'Missed') . "<br>";
}

?>
