// $.ajax({
//   type: "POST",
//   url: "{% url 'home' %}",
//   success: function (response) {
//     console.log(response) //response will be what you send in jsonresponse in django view
//     $('.like-count').innerHtml = `${response.count}`
//   }
// })

$(document).ready(function () {
  const userposts_id1 = $('.like-btn').val();
  console.log(userposts_id1)
  $('#like-form').submit(function (e) {
    e.preventDefault();
    const token = $('input[name=csrfmiddlewaretoken]').val();
    const url = $(this).attr('action')
    $.ajax({
      type: "POST",
      headers: { 'X-CSRFToken': token },
      url: url,
      success: function (response) {
        if (response.liked === true) {
          $('.buton-like').removeClass('btn-primary')
          $('.buton-like').addClass('btn-danger')
          unlike=$('.buton-like').text("Unlike")
          parseInt(unlike)
        }
        else {
          $('.buton-like').removeClass('btn-danger')
          $('.buton-like').addClass('btn-primary')
          like=$('.buton-like').text("Like")
          parseInt(like)
        }
        console.log(response) //response will be what you send in jsonresponse in django view
        // $('.like-count').innerHtml = `${response.count}`
        likecount=$('.like-count').text(response.count)
        console.log(likecount)
          parseInt(likecount)
        // document.getElementById('like-count').innerHTML = response['count'];
      }
    })
  })
})




// $(document).ready(function () {

//   //like ajax call
//   $('.like-form').submit(function (e) {
//     e.preventDefault();
//     const userposts_id = $('.like-btn').val();
//     const token = $('input[name=csrfmiddlewaretoken]').val();
//     const url = $(this).attr('action')
//     $.ajax({
//       method: "POST",
//       url: url,
//       headers: { 'X-CSRFToken': token },
//       data: {
//         'userposts_id': userposts_id
//       }
//     })
//   })
// })