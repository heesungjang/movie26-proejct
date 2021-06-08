// 로그인 함수
function log_in() {
    const username = $("#input-username").val();
    const password = $("#input-password").val();
    console.log(username, password);
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
