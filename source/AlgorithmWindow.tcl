#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Nov 15, 2019 08:16:29 PM -03  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 515x276+650+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Algorithms Window"
    vTcl:DefineAlias "$top" "AlgorithmWindow_Toplevel" vTcl:Toplevel:WidgetProc "" 1
    labelframe $top.lab44 \
        -font TkDefaultFont -foreground black \
        -text {Image smoothing/filtering} -background $vTcl(actual_gui_bg) \
        -height 235 -width 230 
    vTcl:DefineAlias "$top.lab44" "Labelframe1" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    set site_3_0 $top.lab44
    radiobutton $site_3_0.rad45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {2D Convolution} -value 1 \
        -variable filter_radiobutton 
    vTcl:DefineAlias "$site_3_0.rad45" "TwoD_convolution_Radiobutton" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    bind $site_3_0.rad45 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Applies an arbitrary linear filter to an image. When the aperture is partially outside the image, 
the function interpolates outlier pixel values according to the specified border mode.}
    }
    radiobutton $site_3_0.rad46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text Averaging -value 2 -variable filter_radiobutton 
    vTcl:DefineAlias "$site_3_0.rad46" "Averaging_Radiobutton" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    bind $site_3_0.rad46 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Blurs an image using the normalized box filter.}
    }
    radiobutton $site_3_0.rad47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {Gaussian Blurring} -value 3 \
        -variable filter_radiobutton 
    vTcl:DefineAlias "$site_3_0.rad47" "GaussianBlurring_Radiobutton" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    bind $site_3_0.rad47 <<SetBalloon>> {
        set ::vTcl::balloon::%W {It convolves the source image with the specified Gaussian kernel. }
    }
    radiobutton $site_3_0.rad48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {Median Blurring} -value 4 \
        -variable filter_radiobutton 
    vTcl:DefineAlias "$site_3_0.rad48" "MedianBlurring_Radiobutton" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    bind $site_3_0.rad48 <<SetBalloon>> {
        set ::vTcl::balloon::%W {It smoothes an image using the median filter with the ksize×ksize aperture. Each channel of a multi-channel image is processed independently.}
    }
    radiobutton $site_3_0.rad49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {Bilateral Filtering} -value 5 \
        -variable filter_radiobutton 
    vTcl:DefineAlias "$site_3_0.rad49" "BilateralFiltering_Radiobutton" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    bind $site_3_0.rad49 <<SetBalloon>> {
        set ::vTcl::balloon::%W {It can reduce unwanted noise very well while keeping edges fairly sharp. However, it is very slow compared to most filters.}
    }
    radiobutton $site_3_0.rad61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text None -value 0 -variable filter_radiobutton 
    vTcl:DefineAlias "$site_3_0.rad61" "Radiobutton1" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    place $site_3_0.rad45 \
        -in $site_3_0 -x 0 -relx 0.087 -y 60 -width 111 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad46 \
        -in $site_3_0 -x 0 -relx 0.087 -y 90 -width 82 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad47 \
        -in $site_3_0 -x 0 -relx 0.087 -y 120 -width 120 -height 25 \
        -anchor nw -bordermode ignore 
    place $site_3_0.rad48 \
        -in $site_3_0 -x 0 -relx 0.087 -y 150 -width 113 -height 25 \
        -anchor nw -bordermode ignore 
    place $site_3_0.rad49 \
        -in $site_3_0 -x 0 -relx 0.087 -y 180 -width 116 -height 25 \
        -anchor nw -bordermode ignore 
    place $site_3_0.rad61 \
        -in $site_3_0 -x 20 -y 30 -anchor nw -bordermode ignore 
    labelframe $top.lab50 \
        -font TkDefaultFont -foreground black -text {Edge detection} \
        -background $vTcl(actual_gui_bg) -height 175 -width 240 
    vTcl:DefineAlias "$top.lab50" "Labelframe2" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    set site_3_0 $top.lab50
    label $site_3_0.lab51 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Canny algorithm:} 
    vTcl:DefineAlias "$site_3_0.lab51" "Label1" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    bind $site_3_0.lab51 <<SetBalloon>> {
        set ::vTcl::balloon::%W {It finds edges in the input image and marks them in the output map edges using the Canny algorithm. The smallest value between threshold1 and threshold2 is used for edge linking. The largest value is used to find initial segments of strong edges. }
    }
    scale $site_3_0.sca54 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -from 0.0 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 255.0 \
        -troughcolor #d9d9d9 
    vTcl:DefineAlias "$site_3_0.sca54" "Scale1" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    label $site_3_0.lab55 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Thresholding 1} 
    vTcl:DefineAlias "$site_3_0.lab55" "Label2" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    scale $site_3_0.sca56 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -from 0.0 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -orient horizontal -resolution 1.0 -tickinterval 0.0 -to 255.0 \
        -troughcolor #d9d9d9 
    vTcl:DefineAlias "$site_3_0.sca56" "Scale2" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    label $site_3_0.lab57 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Thresholding 2} 
    vTcl:DefineAlias "$site_3_0.lab57" "Label3" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    checkbutton $site_3_0.che59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {L2 Gradient} -variable l2grad 
    vTcl:DefineAlias "$site_3_0.che59" "Checkbutton1" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    bind $site_3_0.che59 <<SetBalloon>> {
        set ::vTcl::balloon::%W {a flag, indicating whether a more accurate L2 norm should be used to calculate the image gradient magnitude, or whether the default L1 norm is enough.}
    }
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.063 -y 30 -anchor nw -bordermode ignore 
    place $site_3_0.sca54 \
        -in $site_3_0 -x 120 -y 40 -width 106 -height 42 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.063 -y 60 -width 84 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.sca56 \
        -in $site_3_0 -x 120 -y 82 -width 106 -height 42 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 20 -y 100 -width 84 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che59 \
        -in $site_3_0 -x 0 -relx 0.063 -y 140 -width 88 -height 25 -anchor nw \
        -bordermode ignore 
    button $top.but60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command apply_settings \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Apply 
    vTcl:DefineAlias "$top.but60" "ApplyAlgorithmSettings_Button" vTcl:WidgetProc "AlgorithmWindow_Toplevel" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab44 \
        -in $top -x 20 -y 20 -width 230 -relwidth 0 -height 235 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 260 -y 20 -width 240 -relwidth 0 -height 175 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 380 -y 220 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
