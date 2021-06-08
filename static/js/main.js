// 로그인 함수
function log_in() {
    const username = $("#input-username").val();
    const password = $("#input-password").val();

    if (username == "") {
        $("#user-input").focus();
        return;
    }

    if (password == "") {
        $("#pass-input").focus();
        return;
    }
    $.ajax({
        type: "POST",
        url: "/auth/login",
        data: {
            username_give: username,
            password_give: password,
        },
        success: function (response) {
            if (response["result"] == "success") {
                $.cookie("mytoken", response["token"], { path: "/" });
                window.location.replace("/");
            } else {
                alert(response["msg"]);
            }
        },
    });
}

function sign_up() {
    const username = $("#input-username").val();
    const email = $("#input-email").val();
    const password = $("#input-password").val();
    const password2 = $("#input-password2").val();

    if (username == "") {
        $("#input-username").focus();
        return;
    }
    if (email == "") {
        $("#input-email").focus();
        return;
    }
    if (password == "") {
        $("#input-password").focus();
        return;
    }
    if (password2 == "") {
        $("#input-password2").focus();
        return;
    }
    console.log(username, email, password, password2);
    $.ajax({
        type: "POST",
        url: "/auth/signup",
        data: {
            username_give: username,
            email_give: email,
            password_give: password,
            password2_give: password2,
        },
        success: function (response) {
            if (response["result"] == "success") {
                alert(response["msg"]);
                window.location.replace("/");
            } else {
                alert(response["msg"]);
            }
        },
    });
}
