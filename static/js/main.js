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
function toggle_like(movie_id, type) {
    console.log(movie_id, type)
    let $a_like = $(`#${movie_id} a[aria-label='heart']`)
    let $i_like = $a_like.find("path")
    if ($i_like.hasClass("fa-heart")) {
        $.ajax({
            type: "POST",
            url: "/movie/1/like",
            data: {
                movie_id_give: movie_id,
                type_give: type,
                action_give: "unlike"
            },
            success: function (response) {
                console.log("unlike")
                $i_like.addClass("fa-heart-o").removeClass("fa-heart")
            }
        })
    } else {
        $.ajax({
            type: "POST",
            url: "/movie/1/like",
            data: {
                post_id_give: post_id,
                type_give: type,
                action_give: "like"
            },
            success: function (response) {
                console.log("like")
                $i_like.addClass("fa-heart").removeClass("fa-heart-o")
            }
        })

    }
}