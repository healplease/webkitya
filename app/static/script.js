updateCSRFtoken = () => {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrf_token"]').val());
            }
        }
    });
};

updateCSRFtoken();

$("#modal-picture").on("show.bs.modal", event => {
    let link = $( event.relatedTarget ).data("link");
    let title = $( event.relatedTarget ).data("title");
    $( event.currentTarget ).find("#modal-title").text(title);
    $( event.currentTarget ).find("#modal-image").attr("src", link);
});

$(document).on( "click", "button[name='btn-edit-album']", event => {
    let album_id = $( event.currentTarget ).closest("li").attr("data-albumid");
    $(`#show-block-${album_id}`).attr('style','display:none !important;');
    $(`#edit-block-${album_id}`).attr('style','display:flex !important;');
    $( event.currentTarget ).closest("li").find("input[name='link_or_album_id']").select();
});

$(document).on( "click", "button[name='btn-discard-album']", event => {
    let album_id = $( event.currentTarget ).closest("li").attr("data-albumid");
    $(`#show-block-${album_id}`).attr('style','display:flex !important;');
    $(`#edit-block-${album_id}`).attr('style','display:none !important;');
});

enableLoader = () => { $( "#spinner" ).fadeTo(150, 1); };
disableLoader = () => { $( "#spinner" ).fadeTo(150, 0); };

sendJSON = (url, data, success) => {
    enableLoader();
    $.ajax({
        type: "POST",
        contentType: 'application/json; charset=utf-8',
        async: false,
        url: url,
        data: JSON.stringify( data ),
        success: success,
    });
    updateCSRFtoken();
};

$(document).on( "click", "button[name='btn-delete-album']", event => {
    let album_id = $( event.currentTarget ).closest("li").attr("data-albumid");
    sendJSON(
        "/admin/delete-album", { album_id: album_id }, 
        () => { $("#albums").load("/admin #albums", disableLoader) }
    );
});


$(document).on( "click", "button[name='btn-save-album']", event => {
    let album_id = $( event.currentTarget ).closest("li").attr("data-albumid");
    let link_or_album_id =  $( event.currentTarget ).closest("li").find("input[name='link_or_album_id']").val();
    sendJSON(
        "/admin/edit-album", { album_id: album_id, link_or_album_id: link_or_album_id }, 
        () => { $("#albums").load("/admin #albums", disableLoader) }
    );
});


$(document).on( "click", "button[name='btn-add-album']", event => {
    let link_or_album_id =  $( event.currentTarget ).closest("li").find("input[name='link_or_album_id']").val();
    sendJSON(
        "/admin/add-album", { link_or_album_id: link_or_album_id }, 
        () => { $("#albums").load("/admin #albums", disableLoader) }
    );
});
