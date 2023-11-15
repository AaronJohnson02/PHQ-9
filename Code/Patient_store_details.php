<?php

// Connect to the database
$db = new PDO('mysql:host=localhost;dbname=patient_database', 'root', '');

echo "Connected to database";

// Get the form data
$patientId = $_POST['patient_id'];
$patientName = $_POST['patient_name'];

// Insert a new record into the Patient_Details table
$query = "INSERT INTO patient_data (Patient_ID, Patient_Name) VALUES (?, ?)";
$stmt = $db->prepare($query);
$stmt->bindParam(1, $patientId);
$stmt->bindParam(2, $patientName);
$stmt->execute();

// Close the database connection
$db = null;

// Redirect to the success page
header('Location: success.php');

?>
