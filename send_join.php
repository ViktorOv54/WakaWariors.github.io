<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "fbi.contact.helpline@gmail.com"; 
    $subject = "New Dragon Boat Club Join Request";

    $name = htmlspecialchars($_POST["name"]);
    $email = htmlspecialchars($_POST["email"]);
    $experience = htmlspecialchars($_POST["experience"]);

    $body = "New join request details:\n\n";
    $body .= "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Experience:\n$experience\n";

    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Message sending failed.";
    }
} else {
    echo "Invalid request.";
}
?>