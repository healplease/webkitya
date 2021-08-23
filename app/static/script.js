$('#modal-picture').on('show.bs.modal', function (event) {
    // Button that triggered the modal
    let button = $(event.relatedTarget)

    // Extract info from data-* attributes
    let link = button.data('link')
    let title = button.data('title')

    console.log(link, title)

    var modal = $(this)
    modal.find('#modal-title').text(title)
    modal.find('#modal-image').attr("src", link)
})
