$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        let access = window.localStorage.getItem('accessToken');
        if (access) {
            console.log(`access=${access}`);
            xhr.setRequestHeader("Authorization", `Bearer ${access}`);
        }
    }
});

function handleAjaxError(rs, e) {
    if (rs.status == 401) {
        if (this.tokenFlag) {
            this.tokenFlag = false;
            if (obtainAccessTokenWithRefreshToken()) {
                this.headers["Authorization"] = `Bearer ${window.localStorage.getItem('accessToken')}`
                $.ajax(this);
            }
        }
    } else {
        console.error(rs.responseText);
    }
}

function getUser() {
    $.ajax({
        type: 'GET',
        url: '/api/auth',
        success: function (response) {
            $("#username").html(response.username);
            $("#user-profile").show();
        },
        error: function (err) {
            $("#user-login").show();

        }
    });
}
$("#logout").click(function (event) {
    window.localStorage.removeItem('refreshToken');
    window.localStorage.removeItem('accessToken');
    window.location.replace("/");
});

function obtainAccessTokenWithRefreshToken() {
    let flag = true;
    let formData = new FormData();
    formData.append('refresh', window.localStorage.getItem('refreshToken'));
    $.ajax({
        url: '/api/token/refresh/',
        type: "POST",
        data: formData,
        async: false,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            window.localStorage.setItem('accessToken', data['access']);
        },
        error: function (rs, e) {
            if (rs.status == 401) {
                flag = false;
                window.location.replace("/login");
            } else {
                console.error(rs.responseText);
            }
        }
    });
    return flag;
}

$(document).ready(function () {
    getUser();
});


$("#login").click(function (event) {
    event.preventDefault();

    let formData = new FormData();
    formData.append('username', $('#login-form [name=username]').val().trim());
    formData.append('password', $('#login-form [name=password]').val().trim());

    $.ajax({
        url: "/api/token/",
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            window.localStorage.setItem('refreshToken', data['refresh']);
            window.localStorage.setItem('accessToken', data['access']);
            window.location.replace("/");
        },
        error: function (err) {
            console.error(err);
            $("#login-feedback-message").text(err.responseJSON.detail);
        }
    });
});
$("#signup").click(function (event) {
    event.preventDefault();

    let formData = new FormData();
    formData.append('username', $('#signup-form [name=username]').val().trim());
    formData.append('email', $('#signup-form [name=email]').val().trim());
    formData.append('name', $('#signup-form [name=name]').val().trim());
    formData.append('password', $('#signup-form [name=password]').val().trim());

    $.ajax({
        url: "/api/auth/",
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            window.location.replace("/");
        },
        error: function (err) {
            console.error(err);
            $("#signup-feedback-message").text(err.responseJSON.detail);
        }
    });
});