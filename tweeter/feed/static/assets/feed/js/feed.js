var localData = undefined;

function getFeed() {
    $.ajax({
        type: 'GET',
        url: '/api/feed',
        success: function (response) {
            localData = response;
            const now = new Date();
            $.each(response, function (index, e) {
                const post_date = new Date(e.published_at);
                const diff = now.getTime() - post_date.getTime();

                let ms = diff;
                const hh = Math.floor(ms / 1000 / 60 / 60);
                ms -= hh * 1000 * 60 * 60;
                const mm = Math.floor(ms / 1000 / 60);
                ms -= mm * 1000 * 60;
                const ss = Math.floor(ms / 1000);
                ms -= ss * 1000;

                let ago;
                if (hh > 24) {
                    ago = `${post_date}`;
                } else if (hh > 0) {
                    ago = `${hh}h`;
                } else if (mm > 0) {
                    ago = `${mm}m`;
                } else {
                    ago = `${ss}s`;
                }

                card = $("<div />", {
                    html: `
                            <div class="card rounded-0">
                                <div class="card-body">
                                    <h6 class="card-title">${e.author.name} <span class="text-muted">@${e.author.username}<span> - ${ago}</h6>
                                    <p class="card-text">${e.post}</p>
                                </div>
                            </div>
                        `});
                $("#feed").append(card);
            });
        },
    });
};

function compareArray(array1, array2) {
    if (array1.lenght != array2.lenght) {
        return false;
    }
    for (let i = 0; i < array1.lenght; ++i) {
        if (JSON.stringify(array1[i]) !== JSON.stringify(array2[i])) {
            return false;
        }
    }
    return true;
}

function checkUpdates() {
    $.ajax({
        type: 'GET',
        url: '/api/feed',
        tokenFlag: true,
        success: function (response) {
            if (compareArray(response, localData)) {
                console.log("Tudo atualizado");
            } else {
                console.log("Nova publicação");
            }
        },
        error: handleAjaxError
    });
}

$(document).ready(function () {
    getFeed();

    setInterval(checkUpdates, 10000);
});

$("#tweet").click(function (e) {
    e.preventDefault();

    let formData = new FormData();

    $("#tweet-form [name]").map(function () {
        formData.append($(this).attr('name'), $(this).val().trim());
    });

    $.ajax({
        url: "/api/feed/",
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function (response) {
            console.log(response);
        }
    });
});