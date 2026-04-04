function togglePassword() {
    let password = document.getElementById("password");

    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
}
function validateForm() {

    let age = document.getElementById("age").value;
    let tsh = document.getElementById("tsh").value;

    if (age <= 0 || age > 120) {
        alert("Invalid Age ❌");
        return false;
    }

    if (tsh < 0) {
        alert("Invalid TSH value ❌");
        return false;
    }

    return true;
}

// AUTO FILL DEMO
function fillDemo() {
    document.getElementsByName("name")[0].value = "Aryan Kumar Singh";
    document.getElementById("age").value = 45;
    document.getElementsByName("sex")[0].value = 1;

    document.getElementById("tsh").value = 2.5;
    document.getElementById("t3").value = 120;
    document.getElementById("tt4").value = 8.5;

    document.getElementsByName("t4u")[0].value = 1.2;
    document.getElementsByName("fti")[0].value = 110;
}