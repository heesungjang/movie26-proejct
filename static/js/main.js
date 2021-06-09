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
                $.cookie("mytoken", response["token"], {path: "/"});
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
                    const movie_id = movie["movie_id"];
                    const poster = movie["image"];
                    const title = movie["title"];
                    const genre = movie["genre"];
                    const producer = movie["producer"];
                    const date = movie["date"];
                    const rate = movie["rate"];
                    const booking = movie["booking"];

                    const temp_html = `
                    <div class="card" >
                        <img
                            class="card-img-top"
                            src="${poster}"
                            alt="Card image cap"
                        />
                        <h5 class="card-title">${title}</h5>
                        <div class="card-body">
                            <div class="card-info">
                                <p>장르: ${genre}</p>
                                <p>감독: ${producer}</p>
                                <p>예매율: ${booking}%</p>
                            </div>
                            <a
                                href="/movie/${movie_id}"
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

function create_comment() {
    const re = /[0-9]/;
    const url = window.location.pathname;

    const movie_id = re.exec(url)[0];

    const comment = $("#input-comment").val();
    const token = $.cookie("mytoken");

    $.ajax({
        type: "POST",
        url: `/movie/${movie_id}/comment`,
        data: {
            comment_give: comment,
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization", "bearer " + token);
        },
        success: function (response) {
            if (response["result"] == "success") {
                alert(response["msg"]);
                location.reload();
            } else {
                alert(response["msg"]);
            }
        },
    });
}

function delete_comment(e) {
    let comment_give = "";
    if (e.target.tagName == "BUTTON") {
        const parent = e.target.parentNode;
        comment_give =
            parent.firstChild.nextSibling.firstChild.nextSibling.textContent;
    } else if (e.target.tagName == "svg") {
        comment_give =
            e.target.parentNode.parentNode.firstChild.nextSibling.firstChild
                .nextSibling.textContent;
    }

    const re = /[0-9]/;
    const url = window.location.pathname;
    const movie_id = re.exec(url)[0];

    $.ajax({
        type: "POST",
        url: `/movie/${movie_id}/comment/delete`,
        data: {
            movie_give: movie_id,
            comment_give: comment_give,
        },
        success: function (response) {
            if (response["result"] == "success") {
                alert(response["msg"]);
                location.reload();
            } else if (response["result"] == "fail") {
                alert(response["msg"]);
            }
        },
    });
}
