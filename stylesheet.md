
    /**
     * Content
     */
    
    body {
    	background-color: #fff;
    	color: #000;
    }
    
    a:active {
    	opacity: 0.7;
    }
    
    .page a.active {
    	opacity: .4;
    }
    
    i,
    em {
    	font-style: italic;
    }
    
    b,
    strong {
    	font-weight: bolder;
    }
    
    sub,
    sup {
    	position: relative;
    	vertical-align: baseline;
    }
    
    sub {
    	top: 0.3em;
    }
    
    sup {
    	top: -0.4em;
    }
    
    s {
    	text-decoration: line-through;
    }
    
    img {
    	border: 0;
    	padding: 0;
    }
    
    ul,
    ol {
    	margin: 0;
    	padding: 0 0 0 1em;
    }
    
    blockquote {
    	margin: 0;
    	padding: 0 0 0 2em;
    }
    
    hr {
    	background: rgba(127, 127, 127, 0.2);
    	border: 0;
    	height: 1px;
    	display: block;
    }
    
    .content img {
    	float: none;
    	margin-bottom: .5em;
    }
    
    .gallery_image_caption {
        margin-top: 1.2rem;
        margin-bottom: 0.5rem;
        font-size: 1.5rem;
    	font-weight: 400;
    	color: rgba(0, 0, 0, 0.35);
    	font-family: Karla, Icons;
    	font-style: normal;
    	line-height: 1.3;	
    }
    
    /**
     * Loading Animation
     */
    
    .loading[data-loading] {
    	position: fixed;
    	bottom: 8px; 
        left: 8px;
    }
    
    /**
     * Editor styles
     */
    
    [data-predefined-style="true"] bodycopy {
    	font-size: 1.4rem;
    	font-weight: 400;
    	color: rgba(0, 0, 0, 0.75);
    	font-family: Karla, Icons;
    	font-style: normal;
    	line-height: 1.3;
    }
    
    [data-predefined-style="true"] bodycopy a {
    	color: rgba(0, 0, 0, 0.75);
    	border-bottom: 1px solid rgba(0, 0, 0, 0.75);
    	text-decoration: none;
    }
    
    [data-predefined-style="true"] bodycopy a:hover {
    
    }
    
    bodycopy a.image-link,
    bodycopy a.icon-link,
    bodycopy a.image-link:hover,
    bodycopy a.icon-link:hover {
    	border-bottom: 0;
    	padding-bottom: 0;
    }
    
    [data-predefined-style="true"] h1 {
    	font-family: Karla, Icons;
    	font-style: normal;
    	font-weight: 400;
    	padding: 0;
    	margin: 0;
    	font-size: 2.8rem;
    	line-height: 1.3;
    	color: rgba(0, 0, 0, 0.85);
    	}
    
    [data-predefined-style="true"] h1 a {
    	color: rgba(0, 0, 0, 0.85);
    }
    
    [data-predefined-style="true"] h2 {
    	font-family: Karla, Icons;
    	font-style: normal;
    	font-weight: 400;
    	padding: 0;
    	margin: 0;
    	color: rgba(0, 0, 0, 0.85);
    	font-size: 2.4rem;
    	line-height: 1.3;
    	}
    
    [data-predefined-style="true"] h2 a {
    	color: rgba(0, 0, 0, 0.85);
    }
    
    [data-predefined-style="true"] small {
    	display: inline-block;
    	font-size: 1.3rem;
    	line-height: 1.3;
    	font-family: 'Space Mono', Icons;
    	font-style: normal;
    	font-weight: 400;
    	color: rgba(0, 0, 0, 0.35);
    }
    
    [data-predefined-style="true"] small a {
    	color: rgb(0, 0, 0);
    	border-bottom-width: 0em;
    }
    
    /**
     * Breakpoints
     */
    
    
    [data-css-preset] .page {
        background-color: initial /*!page_bgcolor*/;
    }
    
    .mobile .page,
    [data-css-preset].mobile .page {
    	position: relative;
    	max-width: 100%;
    	width: 100%;
    	background-color: transparent /*!page_bgcolor*/;
    }
    
    [data-css-preset] .container {
    	margin-left: auto /*!content_right*/;
    	margin-right: 0 /*!content_right*/;
    	text-align: left /*!text_left*/;
    }
    
    [data-css-preset] body {
    	background-color: rgb(255, 255, 255) /*!body_bgcolor*/;
    }
    
    [data-css-preset] .container_width {
    	width: 84% /*!content_right*/;
    }
    
    [data-css-preset] .content_padding {
    	padding-top: 5rem /*!main_margin*/;
    	padding-bottom: 5rem /*!main_margin*/;
    	padding-left: 5rem /*!main_margin*/;
    	padding-right: 5rem /*!main_margin*/;
    }
    
    
    [data-css-preset] text-limit {
    	display: inline-block /*!text_width*/;
    	max-width: 66rem/*!text_width*/;
    }
    
    /**
     * Thumbnails
     */
    
    div[thumbnails] {
    	justify-content: flex-start;
    }
    
    [data-css-preset] .thumbnails {
       	background-color: transparent/*!thumbnails_bgcolor*/;   
    }
    
    [data-css-preset] .thumbnails_width {
        width: 84%/*!thumbnails_width*/;
    }
    
    [data-css-preset] [thumbnails-pad] {
        padding: 1.5rem/*!thumbnails_padding*/;
    }
    
    [data-css-preset] [thumbnails-gutter] {
        margin: -3rem/*!thumbnails_padding*/;
    }
    
    [data-css-preset] [responsive-layout] [thumbnails-pad] {
        padding: 0.75rem/*!responsive_thumbnails_padding*/; 
    }
    
    [data-css-preset] [responsive-layout] [thumbnails-gutter] {
        margin: -1.5rem/*!responsive_thumbnails_padding*/; 
    }
    
    .thumbnails .thumb_image {
    	outline: 0px solid rgba(0,0,0,.12);
        outline-offset: -1px;
    }
    
    .thumbnails .title {
        margin-top: 1.2rem;
        margin-bottom: 0.1rem;
        font-size: 1.4rem;
    	font-weight: 400;
    	color: rgba(0, 0, 0, 0.75);
    	font-family: Karla, Icons;
    	font-style: normal;
    	line-height: 1.1;
    }
    
    .thumbnails .tags {
        margin-top: 1rem;
        margin-bottom: 0.5rem;
        font-size: 1.3rem;
    	font-weight: 400;
    	color: rgba(0, 0, 0, 0.25);
    	font-family: Karla, Icons;
    	font-style: normal;
    	line-height: 1.2;
    }
    
    .thumbnails .tags a {
    	border-bottom: 0;
        color: rgba(0, 0, 0, 0.35);
        text-decoration: none;
    }
    
    .thumbnails .has_title .tags {
    	margin-top: 0rem;
    }
    
    /**
     * Site Menu
     */
    
    [data-css-preset] #site_menu_button {
        color: rgba(0, 0, 0, 0.75);
        line-height: 1;
        font-size: 28px /*!site_menu_button*/;
        padding: 6px;
        line-height: 1;
        background: rgba(33, 32, 46, 0);
        position: fixed;
    	right: 3rem /*!site_menu_button*/;
    	bottom: 3rem /*!site_menu_button*/;
    }
    
    body.mobile #site_menu_button {
    	margin: -6px;
        font-size: 34px;
    }
    
    #site_menu_button.custom_icon {
    	width: 40px;
        height: auto;
    }
    
    #site_menu_button.active {
    	display: none;
    }
    
    
    /**
     * Site Menu
     */
    
    #site_menu {
    	font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif, "Sans Serif", Icons;
    	background: rgba(20, 20, 20, 0.95);
    	font-size: 20px;
    	font-style: normal;
    	font-weight: 400;
    	padding: 20px 30px 90px 30px;
    	max-width: 400px;
    	min-width: 300px;
    	text-align: left;
    	display: flex;
    	justify-content: flex-start;
    }
    
    body.mobile #site_menu {
    	width: 100%;
    }
    
    #site_menu .page-link a {
    	color: rgba(255, 255, 255, 0.75);
    }
    
    #site_menu .set-link > a {
    	color: rgba(255, 255, 255, 0.75);
    	font-weight: bold;
    }
    
    #site_menu a:active {
    	opacity: .7;
    }
    
    #site_menu a.active {
    	opacity: .4;
    }
    
    #site_menu .close {
    	display: none;
    	color: rgba(255, 255, 255, 0.4);
    	line-height: .85em;
    	font-size: 45px;
    }
    
    body.mobile #site_menu .close {
    	display: block;
    	font-size: 50px;
    	line-height: 1em;
    }
    
    #site_menu .break {
    	height: 28px;
    }
    
    #site_menu .indent {
    	margin-left: 28px;
    }
    
    /*
     * Shop Button
     */
    
    [data-css-preset] #shop_button {
    	color: rgba(0, 0, 0, 0.85);
        background: transparent;
    	font-size: 36px;
        font-style: normal;
    	font-weight: 400;
        line-height: 1;
        position: fixed;
    	padding: 6px;
    	top: 5rem /*!shop_button*/;
    	right: 3rem /*!shop_button*/;
    }
    
    #shop_button.text {
        font-size: 1.4rem;
    	font-weight: 400;
    	color: rgba(0, 0, 0, 0.75);
    	font-family: Karla, Icons;
        padding: 0;
        line-height: 1.3;
    }
    
    #shop_button.custom_icon {
    	width: 40px;
        height: auto;
    }
    
    body.mobile #shop_button:not(.text) {
    	margin: -6px;
        font-size: 40px;
    }
    
    /*
     * Shop Product Widget
     */
    
    .shop_product {
        width: 100%;
    	max-width: 22rem;
        position: relative;
        display: block;
    }
    
    .shop_product .price {
    	font-family: Karla, Icons;
    	font-size: 1.4rem;
    	line-height: 1;
    	color: rgba(0, 0, 0, 0.75);
        display: block;
        margin-bottom: 1rem;
    	font-style: normal;
    	font-weight: 400;
    }
    
    .shop_product .dropdown {
        font-family: Karla, Icons;
        font-size: 1.4rem;
        display: inline-block;
    	width: 100%;
        border: 1px solid rgba(0,0,0,.2);
        background:  white url(https://static.cargo.site/assets/images/select-arrows.svg) no-repeat right;
        margin-bottom: 1rem;
        line-height: 1.2;
        padding: .7rem 1rem;
    	font-style: normal;
    	font-weight: 400;
    }
    
    .shop_product .button {
        font-family: Karla, Icons;
    	font-size: 1.4rem;
        background: rgba(0, 0, 0, 0.75);
        color: rgba(255,255,255,1);
        flex: 0 0 50%;
        text-align: left;
        display: inline-block;
    	line-height: 1;
        padding: .8rem 1rem .9rem;
    	font-style: normal;
    	font-weight: 400;
    }
    
    /*
     * Image Zoom
     */
    
    .content img.image-zoom:active {
      opacity: .7;
    }
    
    /**
     * Quick View
     */
    
    [data-css-preset] .quick-view {
        padding-top: 2.5rem /*!quick_view_padding*/;
        padding-bottom: 2.5rem /*!quick_view_padding*/;
        padding-left: 2.5rem /*!quick_view_padding*/;
        padding-right: 2.5rem /*!quick_view_padding*/;
        height: 100% /*!quick_view_height*/;
        width: 100% /*!quick_view_width*/;
    }
    
    body.mobile .quick-view {
        width: 100%;
        height: 100%;
        margin: 0;
    }
    
    
    [data-css-preset] .quick-view-background {
    	background: rgba(0, 0, 0, 0.90) /*!quick_view_bgcolor*/;
    }
    
    .quick-view-caption {
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Open Sans","Helvetica Neue",sans-serif;
        transition: 100ms opacity ease-in-out;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        margin: 2rem 0;
        text-align: center;
        font-size: 1.8rem;
    }
    
    .quick-view-caption span {
        padding: 0.5rem 1rem;
        display: inline-block;
        background: rgba(0,0,0,0.4);
        color: white;
    }
    
    
    /**
     * Quick View Navigation 
     */
    
    .quick-view-navigation .left-arrow {
        left: 10px;
    }
    
    .quick-view-navigation .right-arrow {
        right: 10px;
    }
    
    .quick-view-navigation .left-arrow,
    .quick-view-navigation .right-arrow {
        /* Change height/width together to scale */
        height: 36px;
        width: 36px;
    }
    
    .quick-view-navigation .left-arrow .inner-color,
    .quick-view-navigation .right-arrow .inner-color {
        stroke: #fff;
        stroke-width: 1.5px;
    }
    
    .quick-view-navigation .left-arrow .outer-color,
    .quick-view-navigation .right-arrow .outer-color {
        stroke: #000;
        stroke-width: 2.5px;
        opacity: 0.6;
    }
    
    .quick-view-navigation .close-button {  
        top: 10px;
        right: 10px;
        /* Change height/width together to scale */
        width: 36px;
        height: 36px;
    }
    
    .quick-view-navigation .close-button .inner-color {
        stroke: #fff;
        stroke-width: 1.5px;
    }
    
    .quick-view-navigation .close-button .outer-color {
        stroke: #000;
        stroke-width: 2.5px;
        opacity: 0.6;
    }
    
    /** 
     * Image Gallery Navigation Arrows 
     */
     
    .image-gallery-navigation .left-arrow,
    .image-gallery-navigation .right-arrow {
        /* Change height/width together to scale */
        height: 36px;
        width: 36px;
    }
    
    .image-gallery-navigation .left-arrow .inner-color,
    .image-gallery-navigation .right-arrow .inner-color {
        stroke: #fff;
        stroke-width: 1.5px;
    }
    
    .image-gallery-navigation .left-arrow .outer-color,
    .image-gallery-navigation .right-arrow .outer-color {
        stroke: #000;
        stroke-width: 2.5px;
        opacity: 0.6;
    }
    
    /**
     * Wallpaper Backdrop Navigation Arrows 
     */
    
    .wallpaper-navigation .left-arrow,
    .wallpaper-navigation .right-arrow {
       /* Change height/width together to scale */
       width: 36px;
       height: 36px;
    }
    
    .wallpaper-navigation .left-arrow .inner-color,
    .wallpaper-navigation .right-arrow .inner-color {
       stroke: #fff;
        stroke-width: 1.5px;
    }
    
    .wallpaper-navigation .left-arrow .outer-color,
    .wallpaper-navigation .right-arrow .outer-color {
        stroke: #000;
        stroke-width: 2.5px;
        opacity: 0.6;
    }
    
    
    /**
     * Feed
     */
    
    .feed .content_container .page {
        border-top: 0px dashed rgba(0, 0, 0, 0.2);
    }
    
    .feed .content_container .page_container:first-child .page {
    	border-top: 0;
    }
    
    
    
    /*
     * Audio Player
     */
    
    .audio-player {
        max-width: 36rem;
        height: 3.3rem;
        outline: 1px solid rgba(0,0,0,0.15);
        color: rgba(0, 0, 0, 0.6);
        background: #fff;
        font-size: 1.2rem;
        line-height: 1.3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif, "Sans Serif", Icons;
        font-style: normal;
        font-weight: 400;
        text-align: left;
        margin: 1px 1px 1em 1px;
    }
    
    body.mobile .audio-player {
        max-width: 100%;
    }
    
    .audio-player .separator {
        width: 1px;
        background-color: rgba(0,0,0,0.15);
    }
    
    .audio-player .button {
        background: transparent;
        cursor: pointer;
        fill: rgba(0, 0, 0, 0.85);
    }
    
    .audio-player .icon {
        fill: rgba(0, 0, 0, 0.85);
        padding: 30%;
        width: 100%;
        margin: auto;
    }
    
    .audio-player .buffer {
        background: rgba(0,0,0,0.03);
    }
    
    .audio-player .progress {
        background: rgba(0,0,0,0.1);
    }
    
    .audio-player .progress-indicator {
        border: 1px solid rgba(0, 0, 0, 0.7);
        width: 1px;
        height: 100%;
        right: 0;
        position: absolute;
        cursor: ew-resize;
    }
    
    .audio-player .note-icon {
        height: 100%;
        width: 3.8rem;
        padding: 1rem;
        fill: rgba(0, 0, 0, 0.5);
    }
    
    .audio-player .current-time {
        padding-left: 1rem;
    }
    
    .audio-player .total-time {
        padding-right: 1rem;
    }
    
    
    

