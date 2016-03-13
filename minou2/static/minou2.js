$(function(){
  'use strict';
  var on_complete_analysis = function(images) {
    images.forEach(function(image) {
      $('#image').append('<img src="'+image.preview+'" width="100px"/>');
    });
  }

  $('#magic').click(function(){
    var text = $('#editor').val();
    $.post('/anal', {text: text}, function(data) {
      var anal_job = data.job;
      var check_anal = function() {
        $.get('/anal/' + anal_job, function(data) {
          if(data.result) {
            $.post('/search', {analysis: anal_job}, function(data) {
              var search_job = data.job;
              var check_search = function() {
                $.get('/search/' + search_job, function(response) {
                  if(response.result) {
                    on_complete_analysis(response.result);
                  } else {
                    setTimeout(check_search, 1000);
                  }
                });
              }
              setTimeout(check_search, 1000);
            });
          } else {
            setTimeout(check_anal, 1000);
          }
        });
      }
      setTimeout(check_anal, 1000);
    })
  });
});
