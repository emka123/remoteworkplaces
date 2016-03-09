 $(document).ready(function(){
 	 $('a[href^="#"]').click(function() {
        var hash = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(hash).offset().top - 50
        }, 500);
        return false;
    });
 });
	 