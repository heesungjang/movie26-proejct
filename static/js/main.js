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

function get_movies() {
    $.ajax({
        type: "GET",
        url: "/movie/list",
        data: {},
        success: function (response) {
            if (response["msg"] == "success") {
                const movies = response.movies;
                movies.map((movie) => {
                    const poster = movie["image"];
                    const title = movie["title"];
                    const genre = movie["genre"];
                    const producer = movie["producer"];
                    const date = movie["date"];
                    const rate = movie["rate"];
                    const booking = movie["booking"];

                    const temp_html = `
                            <div class="card" style="width: 18rem">
                        <img
                            class="card-img-top"
                            src="${poster}"
                            alt="Card image cap"
                        />
                        <div style="margin-left: 10px" class="card-body">
                            <span style="font-size: 20px" class="card-title"
                                >${title}</span
                            >
                            <span
                                style="display: block; font-size: 10px"
                                class="card-title"
                                >장르: ${genre}</span
                            >
                            <span
                                style="
                                    font-size: 13px;
                                    display: block;
                                    margin: 5px 0 0 0;
                                "
                                class="card-text"
                                >감독: ${producer}</span
                            >
                            <span
                                style="font-size: 12px; display: block"
                                class="card-title"
                                >예매율: ${booking}%</span
                            >
                            <a
                                style="
                                    display: block;
                                    text-align: end;
                                    margin-right: 20px;
                                    color: inherit;
                                    font-weight: 700;
                                    height: 35px;
                                "
                                href="#"
                                class="btn btn-primary"
                                >상세보기</a
                            >
                        </div>
                    </div>
                    `;
                    if (title != "") {
                        $("#movies-box").append(temp_html);
                    }
                });
            } else {
                alert(response["msg"]);
            }
        },
    });
}
