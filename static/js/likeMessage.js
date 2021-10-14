$(document).ready(function () {
    // const usermessages_id = $('.btn-like').val();
    $('.like-form-message').submit(function (e) {
      e.preventDefault();
      // const usermessages_id = $('.btn-like').val();
      const token = $('input[name=csrfmiddlewaretoken]').val();
      const url = $(this).attr('action');
      const id = $(this).attr('name');
      $.ajax({
        type: "POST",
        headers: { 'X-CSRFToken': token },
        url: url,
        id: id,
        data: {
          "id":id,
          "url":url,
        },
        success: function (response) {
          if (response.liked === true) {
            $(".btn-like" + id).removeClass('btn-primary')
            $(".btn-like" + id).addClass('btn-danger')
            unlike=$(".btn-like" + id).text("Unlike")
            parseInt(unlike)
          }
          else {
            $(".btn-like" + id).removeClass('btn-danger')
            $(".btn-like" + id).addClass('btn-primary')
            like=$(".btn-like" + id).text("Like")
            parseInt(like)
          }
          // $('.like-count').innerHtml = `${response.count}`
          likecount=$('.messageTotal'+id).text(response.count1)
          parseInt(likecount)
          // document.getElementById('like-count').innerHTML = response['count'];
        }
      })
    })
  })
  