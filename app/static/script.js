///////////////////////////////////////////////////////
// csrf token update

updateCSRFtoken = () => {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrf_token"]').val());
            }
        }
    });
};

///////////////////////////////////////////////////////
// easier json send for admin

enableLoader = () => { $( "#spinner" ).fadeTo(150, 1); };
disableLoader = () => { $( "#spinner" ).fadeTo(150, 0); };

sendJSON = (url, data, complete) => {
    enableLoader();
    $.ajax({
        type: "POST",
        contentType: 'application/json; charset=utf-8',
        async: false,
        url: url,
        data: JSON.stringify( data ),
        complete: complete,
    });
    updateCSRFtoken();
};

///////////////////////////////////////////////////////

$(function () {$('[data-toggle="tooltip"]').tooltip() });
updateCSRFtoken();

///////////////////////////////////////////////////////
// view picture in modal window

$("#modal-picture").on("show.bs.modal", event => {
    let link = $( event.relatedTarget ).data("link");
    let title = $( event.relatedTarget ).data("title");
    $( event.currentTarget ).find("#modal-title").text(title);
    $( event.currentTarget ).find("#modal-image").attr("src", link);
});

///////////////////////////////////////////////////////
// on edit album - show edit block and hide view block

$(document).on( "click", "button[name='btn-edit-album']", event => {
    $( event.currentTarget ).closest("li").find("div[role='view']").attr('style','display:none !important;');
    $( event.currentTarget ).closest("li").find("div[role='edit']").attr('style','display:flex !important;');
    $( event.currentTarget ).closest("li").find("input[name='link_or_album_id']").select();
});

///////////////////////////////////////////////////////
// on discard album - show view block and hide edit block

$(document).on( "click", "button[name='btn-discard-album']", event => {
    $( event.currentTarget ).closest("li").find("div[role='edit']").attr('style','display:none !important;');
    $( event.currentTarget ).closest("li").find("div[role='view']").attr('style','display:flex !important;');
});

///////////////////////////////////////////////////////
// on delete album - send ajax request 

$(document).on( "click", "button[name='btn-delete-album']", event => {
    let album_id = $( event.currentTarget ).closest("li").attr("data-albumid");
    sendJSON(
        "/admin/delete-album", { album_id: album_id }, 
        () => { $("#albums").load("/admin #albums", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on save album - send ajax request

$(document).on( "click", "button[name='btn-save-album']", event => {
    let album_id = $( event.currentTarget ).closest("li").attr("data-albumid");
    let link_or_album_id =  $( event.currentTarget ).closest("li").find("input[name='link_or_album_id']").val();
    sendJSON(
        "/admin/edit-album", { album_id: album_id, link_or_album_id: link_or_album_id }, 
        () => { $("#albums").load("/admin #albums", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on add album - send ajax request

$(document).on( "click", "button[name='btn-add-album']", event => {
    let link_or_album_id =  $( event.currentTarget ).closest("li").find("input[name='link_or_album_id']").val();
    sendJSON(
        "/admin/add-album", { link_or_album_id: link_or_album_id }, 
        () => { $("#albums").load("/admin #albums", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on edit media - show edit block and hide view block

$(document).on( "click", "button[name='btn-edit-media']", event => {
    $( event.currentTarget ).closest("li").find("div[role='view']").attr('style','display:none !important;');
    $( event.currentTarget ).closest("li").find("div[role='edit']").attr('style','display:flex !important;');
    $( event.currentTarget ).closest("li").find("input[name='media_link']").select();
});

///////////////////////////////////////////////////////
// on discard media - show view block and hide edit block

$(document).on( "click", "button[name='btn-discard-media']", event => {
    $( event.currentTarget ).closest("li").find("div[role='edit']").attr('style','display:none !important;');
    $( event.currentTarget ).closest("li").find("div[role='view']").attr('style','display:flex !important;');
});

///////////////////////////////////////////////////////
// on delete media - send ajax request 

$(document).on( "click", "button[name='btn-delete-media']", event => {
    let link_to_delete = $( event.currentTarget ).closest("li").attr("data-link");
    sendJSON(
        "/admin/delete-media", { link: link_to_delete }, 
        () => { $("#social-media").load("/admin #social-media", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on save media - send ajax request

$(document).on( "click", "button[name='btn-save-media']", event => {
    let link_to_update = $( event.currentTarget ).closest("li").attr("data-link");
    let link =  $( event.currentTarget ).closest("li").find("input[name='media_link']").val();
    let icon =  $( event.currentTarget ).closest("li").find("input[name='media_icon']").val();
    sendJSON(
        "/admin/edit-media", { updated: link_to_update, link: link, icon: icon }, 
        () => { $("#social-media").load("/admin #social-media", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on add media - send ajax request

$(document).on( "click", "button[name='btn-add-media']", event => {
    let link =  $( event.currentTarget ).closest("li").find("input[name='media_link']").val();
    let icon =  $( event.currentTarget ).closest("li").find("input[name='media_icon']").val();
    sendJSON(
        "/admin/add-media", { link: link, icon: icon }, 
        () => { $("#social-media").load("/admin #social-media", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on edit user - show edit block and hide view block

$(document).on( "click", "button[name='btn-edit-admin']", event => {
    $( event.currentTarget ).closest("li").find("div[role='view']").attr('style','display:none !important;');
    $( event.currentTarget ).closest("li").find("div[role='edit']").attr('style','display:flex !important;');
    $( event.currentTarget ).closest("li").find("input[name='old_password']").select();
});

///////////////////////////////////////////////////////
// on discard user - show view block and hide edit block

$(document).on( "click", "button[name='btn-discard-admin']", event => {
    $( event.currentTarget ).closest("li").find("div[role='edit']").attr('style','display:none !important;');
    $( event.currentTarget ).closest("li").find("div[role='view']").attr('style','display:flex !important;');
});

///////////////////////////////////////////////////////
// on delete user - send ajax request 

$(document).on( "click", "button[name='btn-delete-admin']", event => {
    let username = $( event.currentTarget ).closest("li").attr("data-username");
    sendJSON(
        "/admin/delete-admin", { username: username }, 
        () => { $("#access").load("/admin #access", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on save user - send ajax request

$(document).on( "click", "button[name='btn-save-admin']", event => {
    let username = $( event.currentTarget ).closest("li").attr("data-username");
    let old_password = $( event.currentTarget ).closest("li").find("input[name='old_password']").val();
    let new_password = $( event.currentTarget ).closest("li").find("input[name='new_password']").val();
    let disabled = $( event.currentTarget ).closest("li").find("input[name='disabled']").is(":checked");
    sendJSON(
        "/admin/edit-admin", { username: username, old_password: old_password, new_password: new_password, disabled: disabled }, 
        () => { $("#access").load("/admin #access", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on add user - send ajax request

$(document).on( "click", "button[name='btn-add-admin']", event => {
    let username = $( event.currentTarget ).closest("li").find("input[name='username']").val();
    let password = $( event.currentTarget ).closest("li").find("input[name='password']").val();
    let disabled = $( event.currentTarget ).closest("li").find("input[name='disabled']").is(":checked");
    sendJSON(
        "/admin/add-admin", { username: username, password: password, disabled: disabled }, 
        () => { $("#access").load("/admin #access", disableLoader) }
    );
});

///////////////////////////////////////////////////////
// on save cols count - send ajax request 

$(document).on( "click", "button[name='btn-save-cols']", event => {
    let value =  $( event.currentTarget ).closest("div.d-flex").find("input[name='columns']:checked").val();
    sendJSON(
        "/admin/change-cols", { cols: value },
        () => { $("#columns").load("/admin #columns", disableLoader) }
    );
});
