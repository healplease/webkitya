$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", document.querySelector('meta[name="csrf-token"]').content);
        }
    }
});

$("#modal-picture").on("show.bs.modal", event => {
    // Button that triggered the modal
    let button = $(event.relatedTarget);

    // Extract info from data-* attributes
    let link = button.data("link");
    let title = button.data("title");

    console.log(link, title)

    let modal = $(this)
    modal.find("#modal-title").text(title);
    modal.find("#modal-image").attr("src", link);
})

$("button[name='btn-edit']").click( event => {
    let album_id = $( event.currentTarget ).closest("li[data-albumid]").attr("data-albumid");
    $(`#show-block-${album_id}`).attr('style','display:none !important;');
    $(`#edit-block-${album_id}`).attr('style','display:flex !important;');
});

$("button[name='btn-discard']").click( event => {
    let album_id = $( event.currentTarget ).closest("li[data-albumid]").attr("data-albumid");
    $(`#show-block-${album_id}`).attr('style','display:flex !important;');
    $(`#edit-block-${album_id}`).attr('style','display:none !important;');
});
