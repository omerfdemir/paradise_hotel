(function($) {

	"use strict";


	//Hide Loading Box (Preloader)
	function handlePreloader() {
		if($('.preloader').length){
			$('.preloader').delay(200).fadeOut(500);
		}
	}


	//Update header style + Scroll to Top
	function headerStyle() {
		if($('.main-header').length){
			var mainHeader = $('.main-header').height();
			var windowpos = $(window).scrollTop();
			if (windowpos >= mainHeader) {
				$('.sticky-header').addClass('now-visible');
				$('.scroll-to-top').fadeIn(300);
			} else {
				$('.sticky-header').removeClass('now-visible');
				$('.scroll-to-top').fadeOut(300);
			}
		}
	}

	headerStyle();


	//Submenu Dropdown Toggle
	if($('.main-header li.dropdown ul').length){
		$('.main-header li.dropdown').append('<div class="dropdown-btn"></div>');

		//Dropdown Button
		$('.main-header li.dropdown .dropdown-btn').on('click', function() {
			$(this).prev('ul').slideToggle(500);
		});


		//Disable dropdown parent link
		$('.navigation li.dropdown > a').on('click', function(e) {
			e.preventDefault();
		});
	}


	//Revolution Slider
	if($('.main-slider .tp-banner').length){

		jQuery('.main-slider .tp-banner').show().revolution({
			delay:10000,
			startwidth:1200,
			startheight:720,
			hideThumbs:600,

			thumbWidth:80,
			thumbHeight:50,
			thumbAmount:5,

			navigationType:"bullet",
			navigationArrows:"0",
			navigationStyle:"preview4",

			touchenabled:"on",
			onHoverStop:"off",

			swipe_velocity: 0.7,
			swipe_min_touches: 1,
			swipe_max_touches: 1,
			drag_block_vertical: false,

			parallax:"mouse",
			parallaxBgFreeze:"on",
			parallaxLevels:[7,4,3,2,5,4,3,2,1,0],

			keyboardNavigation:"off",

			navigationHAlign:"center",
			navigationVAlign:"bottom",
			navigationHOffset:0,
			navigationVOffset:20,

			soloArrowLeftHalign:"left",
			soloArrowLeftValign:"center",
			soloArrowLeftHOffset:20,
			soloArrowLeftVOffset:0,

			soloArrowRightHalign:"right",
			soloArrowRightValign:"center",
			soloArrowRightHOffset:20,
			soloArrowRightVOffset:0,

			shadow:0,
			fullWidth:"on",
			fullScreen:"off",

			spinner:"spinner4",

			stopLoop:"off",
			stopAfterLoops:-1,
			stopAtSlide:-1,

			shuffle:"off",

			autoHeight:"off",
			forceFullWidth:"on",

			hideThumbsOnMobile:"on",
			hideNavDelayOnMobile:1500,
			hideBulletsOnMobile:"on",
			hideArrowsOnMobile:"on",
			hideThumbsUnderResolution:0,

			hideSliderAtLimit:0,
			hideCaptionAtLimit:0,
			hideAllCaptionAtLilmit:0,
			startWithSlide:0,
			videoJsPath:"",
			fullScreenOffsetContainer: ""
	  });

	}


	//Tabs Box
	if($('.tabs-box').length){

		//Tabs
		$('.tabs-box .tab-buttons .tab-btn').on('click', function() {
			
			var target = $($(this).attr('href'));

			target.parents('.tabs-box').children('.tab-buttons').children('.tab-btn').removeClass('active-btn');
			$(this).addClass('active-btn');
			target.parents('.tabs-box').children('.tab-content').children('.tab').fadeOut(0);
			target.parents('.tabs-box').children('.tab-content').children('.tab').removeClass('active-tab');
			$(target).fadeIn(300);
			$(target).addClass('active-tab');
		});

	}


	//Sortable Masonary with Filters
	function enableMasonry() {
		if($('.sortable-masonry').length){

			var winDow = $(window);
			// Needed variables
			var $container=$('.sortable-masonry .items-container');
			var $filter=$('.filter-btns');

			$container.isotope({
				filter:'*',
				 masonry: {
					columnWidth : 2
				 },
				animationOptions:{
					duration:500,
					easing:'linear'
				}
			});


			// Isotope Filter
			$filter.find('li').on('click', function(){
				var selector = $(this).attr('data-filter');

				try {
					$container.isotope({
						filter	: selector,
						animationOptions: {
							duration: 500,
							easing	: 'linear',
							queue	: false
						}
					});
				} catch(err) {

				}
				return false;
			});


			winDow.bind('resize', function(){
				var selector = $filter.find('li.active').attr('data-filter');

				$container.isotope({
					filter	: selector,
					animationOptions: {
						duration: 500,
						easing	: 'linear',
						queue	: false
					}
				});
			});


			var filterItemA	= $('.filter-btns li');

			filterItemA.on('click', function(){
				var $this = $(this);
				if ( !$this.hasClass('active')) {
					filterItemA.removeClass('active');
					$this.addClass('active');
				}
			});
		}
	}

	enableMasonry();


	// Nearby Locations Map
	if($('#locations-box').length){

		$('#locations-box').gMap({
			controls: false,
			scrollwheel: false,
			maptype: 'ROADMAP', // 'HYBRID', 'SATELLITE', 'ROADMAP' or 'TERRAIN'
			markers: [
				{
					latitude: 24.062040,
					longitude: 89.871008,
					icon: {
						image: "images/icons/marker-one.png",
						iconsize: [62, 84],
						iconanchor: [62,84]
					}
				},
				{
					latitude: 23.997445,
					longitude: 89.853155,
					icon: {
						image: "images/icons/marker-two.png",
						iconsize: [62, 84],
						iconanchor: [62,84]
					}
				},
				{
					latitude: 23.980507,
					longitude: 89.984305,
					icon: {
						image: "images/icons/marker-three.png",
						iconsize: [62, 84],
						iconanchor: [62,84]
					}
				},
				{
					latitude: 23.937838,
					longitude: 90.039923,
					icon: {
						image: "images/icons/marker-four.png",
						iconsize: [62, 84],
						iconanchor: [62,84]
					}
				}
			],
			icon: {
				image: "images/icons/map-marker.png",
				iconsize: [62, 84],
				iconanchor: [62,84]
			},
			latitude: 24.062040,
			longitude: 89.871008,
			zoom: 11
		});
	}


	//Testimonials Carousel Slider
	if ($('.testimonials-carousel').length) {
		$('.testimonials-carousel').owlCarousel({
			loop:true,
			margin:60,
			nav:true,
			autoplayHoverPause:false,
			autoplay: 5000,
			smartSpeed: 700,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:1
				},
				760:{
					items:2
				},
				1024:{
					items:3
				},
				1100:{
					items:3
				}
			}
		});
	}


	//Mixitup Gallery
	if($('.filter-list').length){
		$('.filter-list').mixItUp({});
	}


	//Tour Gallery Slider
	if($('#tour-gallery').length){
		var slider = new MasterSlider();
		slider.setup('masterslider' , {
			width:1170,
			height:560,
			space:10,
			preload:3,
			view:'basic'
		});
		slider.control('arrows');

		var gallery = new MSGallery('tour-gallery' , slider);
		gallery.setup();
	}


	//Accordion Box
	if($('.accordion-box').length){
		$(".accordion-box").on('click', '.accord-btn', function() {

			var target = $(this).parents('.accordion');

			if($(this).hasClass('active')!==true){
			$('.accordion .accord-btn').removeClass('active');

			}

			if ($(this).next('.accord-content').is(':visible')){
				//$(this).removeClass('active');
				return false;
				//$(this).next('.accord-content').slideUp(300);
			}else{
				$(this).addClass('active');
				$('.accordion').removeClass('active-block');
				$('.accordion .accord-content').slideUp(300);
				target.addClass('active-block');
				$(this).next('.accord-content').slideDown(300);
			}
		});
	}


	//Sponsors Slider
	if ($('.sponsors-slider').length) {
		$('.sponsors-slider').owlCarousel({
			loop:true,
			margin:0,
			nav:true,
			smartSpeed: 500,
			autoplay: 4000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				480:{
					items:2
				},
				600:{
					items:2
				},
				800:{
					items:3
				},
				1200:{
					items:4
				}
			}
		});
	}


	//LightBox / Fancybox
	if($('.lightbox-image').length) {
		$('.lightbox-image').fancybox({
			openEffect  : 'elastic',
			closeEffect : 'elastic',
			helpers : {
				media : {}
			}
		});
	}


	//Contact Form Validation
	if($('#contact-form').length){
		$('#contact-form').validate({
			rules: {
				username: {
					required: true
				},
				email: {
					required: true,
					email: true
				},
				phone: {
					required: true
				},
				message: {
					required: true
				}
			}
		});
	}


	// Scroll to a Specific Div
	if($('.scroll-to-target').length){
		$(".scroll-to-target").on('click', function() {
			var target = $(this).attr('data-target');
		   // animate
		   $('html, body').animate({
			   scrollTop: $(target).offset().top
			 }, 1000);

		});
	}


	// Elements Animation
	if($('.wow').length){
		var wow = new WOW(
		  {
			boxClass:     'wow',      // animated element css class (default is wow)
			animateClass: 'animated', // animation css class (default is animated)
			offset:       0,          // distance to the element when triggering the animation (default is 0)
			mobile:       true,       // trigger animations on mobile devices (default is true)
			live:         true       // act on asynchronously loaded content (default is true)
		  }
		);
		wow.init();
	}


/* ==========================================================================
   When document is Scrollig, do
   ========================================================================== */

	$(window).on('scroll', function() {
		headerStyle();
	});

/* ==========================================================================
   When document is loaded, do
   ========================================================================== */

	$(window).on('load', function() {
		handlePreloader();
		enableMasonry();
	});



})(window.jQuery);
