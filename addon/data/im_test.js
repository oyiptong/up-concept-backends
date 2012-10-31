

$(document).ready(function () {

  console.log( "READY" );
	$("#image_test").submit(function(e) {
    e.preventDefault();
    let cat = $("#cat_input").attr("value");
    self.port.emit("get_image",cat);
    //e.stopPropagation();
	});

});


self.port.on ( "show_image", function(imageUrl) {
  console.log("new url " + imageUrl);
  $("#cat_image").attr("src",imageUrl);
});

