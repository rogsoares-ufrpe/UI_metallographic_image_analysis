#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  May 16, 2024 05:57:55 PM -03  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) white
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 0
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
set vTcl(project_theme) page-legacy



proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu $top.m53 -background #d9d9d9 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 1290x690+64+108
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 825
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "MEDIA - Metallographic Digital Image Analyzer"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel_MainWindow" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m53" \
        -activebackground #ececec -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    
set site_3_0 $top.m53
    $top.m53 add cascade \
        -menu "$top.m53.men54" -command "{}" -compound left -label "File" 
    menu "$site_3_0.men54" \
        -activebackground beige -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    $site_3_0.men54 add command \
        -command "#open_image_file" -compound left -label "Open image file" 
    $site_3_0.men54 add command \
        -command "#exporttoxlxs" -compound left -label "Export to Excel" 
    $site_3_0.men54 add separator \
        
    $site_3_0.men54 add command \
        -command "#close_application" -compound left -label "Quit" 
    
set site_3_0 $top.m53
    $top.m53 add cascade \
        -menu "$top.m53.men51" -command "{}" -compound left -label "Image analysis" 
    menu "$site_3_0.men51" \
        -activebackground beige -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    $site_3_0.men51 add command \
        -command "#open_segmentation_panel" -compound left \
        -label "Segmentation Panel" 
    $site_3_0.men51 add command \
        -command "#open_procedure_panel" -compound left \
        -label "Measuring procedures" 
    
set site_3_0 $top.m53
    $top.m53 add cascade \
        -menu "$top.m53.men55" -command "{}" -compound left -label "Help" 
    menu "$site_3_0.men55" \
        -activebackground beige -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    $site_3_0.men55 add command \
        -command "#" -compound left -label "Tutorial" 
    $site_3_0.men55 add separator \
        
    $site_3_0.men55 add command \
        -command "#about" -compound left -label "About" 
    frame "$top.fra47" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 670 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 1279 
    vTcl:DefineAlias "$top.fra47" "MainFrame" vTcl:WidgetProc "Toplevel_MainWindow" 1
    set site_3_0 $top.fra47
    label "$site_3_0.lab49" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "File directory path:" 
    vTcl:DefineAlias "$site_3_0.lab49" "LabelTextPath" vTcl:WidgetProc "Toplevel_MainWindow" 1
    canvas "$site_3_0.can48" \
        -background #d9d9d9 -borderwidth 2 -closeenough 1.0 -height 610 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -relief ridge -selectbackground #c4c4c4 \
        -selectforeground black -width 800 
    vTcl:DefineAlias "$site_3_0.can48" "MainCanvas" vTcl:WidgetProc "Toplevel_MainWindow" 1
    canvas "$site_3_0.can60" \
        -background #d9d9d9 -borderwidth 2 -closeenough 1.0 -height 313 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -relief ridge -selectbackground #c4c4c4 \
        -selectforeground black -width 450 
    vTcl:DefineAlias "$site_3_0.can60" "CanvasHistogram" vTcl:WidgetProc "Toplevel_MainWindow" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd "$site_3_0.scr48" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 285 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 450 
    vTcl:DefineAlias "$site_3_0.scr48" "TextBox_output" vTcl:WidgetProc "Toplevel_MainWindow" 1

    $site_3_0.scr48.01 configure -background white \
        -font "-family {Courier New} -size 10" \
        -foreground #000000 \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #000000 \
        -insertbackground #000000 \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    label "$site_3_0.lab50" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "<vazio>" 
    vTcl:DefineAlias "$site_3_0.lab50" "LabelDirectoryPathName" vTcl:WidgetProc "Toplevel_MainWindow" 1
    place $site_3_0.lab49 \
        -in $site_3_0 -x 10 -y 620 -width 0 -relwidth 0.091 -height 0 \
        -relheight 0.031 -anchor nw -bordermode ignore 
    place $site_3_0.can48 \
        -in $site_3_0 -x 10 -y 10 -width 800 -relwidth 0 -height 610 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.can60 \
        -in $site_3_0 -x 814 -y 310 -width 450 -relwidth 0 -height 310 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr48 \
        -in $site_3_0 -x 815 -y 12 -width 450 -relwidth 0 -height 285 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 10 -y 640 -width 0 -relwidth 0.694 -height 0 \
        -relheight 0.031 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra47 \
        -in $top -x 10 -y 10 -width 1274 -relwidth 0 -height 670 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top2 {base} {
    global vTcl
    if {$base == ""} {
        set base .top2
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu $top.m47 -background #d9d9d9 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 521x223+960+82
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 845
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Segmentation settings"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "TopLevel_SegmentationWindow" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m47" \
        -activebackground #ececec -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    labelframe "$top.lab47" \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -text "Segmentation" -background #d9d9d9 -height 205 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 500 
    vTcl:DefineAlias "$top.lab47" "LabelFrame_Segmentation" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    set site_3_0 $top.lab47
    labelframe "$site_3_0.lab47" \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -text "Filters" -background #d9d9d9 -height 175 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 140 
    set site_4_0 $site_3_0.lab47
    radiobutton "$site_4_0.rad47" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_filter" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "None" -value "1" -variable "rb_filter" 
    vTcl:DefineAlias "$site_4_0.rad47" "RadioButton_Filter_None" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    radiobutton "$site_4_0.rad48" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_filter" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "Gaussian Blur" -value "2" -variable "rb_filter" 
    vTcl:DefineAlias "$site_4_0.rad48" "RadioButton_Filter_GaussianBlur" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    radiobutton "$site_4_0.rad49" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_filter" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "2D Convolution" -value "3" -variable "rb_filter" 
    vTcl:DefineAlias "$site_4_0.rad49" "RadioButton_Filter_2DConvolution" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    radiobutton "$site_4_0.rad50" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_filter" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "Bilateral" -value "4" -variable "rb_filter" 
    vTcl:DefineAlias "$site_4_0.rad50" "Radiobutton_Filter_Bilateral" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    radiobutton "$site_4_0.rad51" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_filter" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "Median Blur" -value "5" -variable "rb_filter" 
    vTcl:DefineAlias "$site_4_0.rad51" "Radiobutton_Filter_MedianBlur" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    radiobutton "$site_4_0.rad52" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_filter" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "Binary" -value "7" -variable "rb_filter" 
    vTcl:DefineAlias "$site_4_0.rad52" "Radiobutton_Filter_Laplacian" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    radiobutton "$site_4_0.rad53" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_filter" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "Averaging" -value "6" -variable "rb_filter" 
    vTcl:DefineAlias "$site_4_0.rad53" "Radiobutton_Averaging" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    place $site_4_0.rad47 \
        -in $site_4_0 -x 10 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.rad48 \
        -in $site_4_0 -x 10 -y 40 -anchor nw -bordermode ignore 
    place $site_4_0.rad49 \
        -in $site_4_0 -x 10 -y 60 -anchor nw -bordermode ignore 
    place $site_4_0.rad50 \
        -in $site_4_0 -x 10 -y 80 -anchor nw -bordermode ignore 
    place $site_4_0.rad51 \
        -in $site_4_0 -x 10 -y 100 -anchor nw -bordermode ignore 
    place $site_4_0.rad52 \
        -in $site_4_0 -x 10 -y 140 -anchor nw -bordermode ignore 
    place $site_4_0.rad53 \
        -in $site_4_0 -x 10 -y 120 -anchor nw -bordermode ignore 
    labelframe "$site_3_0.lab53" \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -text "Edge detection method" -background #d9d9d9 -height 55 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 170 
    vTcl:DefineAlias "$site_3_0.lab53" "Labelframe_Edgedetection" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    set site_4_0 $site_3_0.lab53
    ttk::style map TCombobox -background  [list !disabled #d9d9d9 disabled #d9d9d9]  -arrowcolor  [list disabled #000000 !disabled #d9d9d9]
    ttk::combobox "$site_4_0.tCo51" \
        -values "Canny Sobel Prewitt" -font "-family {Segoe UI} -size 9" \
        -textvariable "edge_detection_var" 
    vTcl:DefineAlias "$site_4_0.tCo51" "ComboBox_EdgeDetectionMethods" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    place $site_4_0.tCo51 \
        -in $site_4_0 -x 10 -y 20 -anchor nw -bordermode ignore 
    labelframe "$site_3_0.lab48" \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -text "Mean and STD amplification" -background #d9d9d9 -height 55 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 170 
    set site_4_0 $site_3_0.lab48
    label "$site_4_0.lab49" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 
    ttk::style map TCombobox -background  [list !disabled #d9d9d9 disabled #d9d9d9]  -arrowcolor  [list disabled #000000 !disabled #d9d9d9]
    ttk::combobox "$site_4_0.tCo53" \
        -values "1 2 3 4 5 6 7 8 9 10" -font "-family {Segoe UI} -size 9" \
        -textvariable "meanSTD_var" 
    vTcl:DefineAlias "$site_4_0.tCo53" "ComboBox_MeanSTD" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    place $site_4_0.lab49 \
        -in $site_4_0 -x 10 -y 30 -anchor nw -bordermode ignore 
    place $site_4_0.tCo53 \
        -in $site_4_0 -x 10 -y 20 -width 43 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    button "$site_3_0.but47" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -command "open_data_image_window" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -pady 0 -text "Data image" 
    vTcl:DefineAlias "$site_3_0.but47" "ButtonDataImage" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    bind $site_3_0.but47 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Opens the data image window}
    }
    button "$site_3_0.but48" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -command "start_grains_segmentation" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -pady 0 -text "Apply" 
    vTcl:DefineAlias "$site_3_0.but48" "ButtonApplySgmentation" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    labelframe "$site_3_0.lab49" \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -text "Dsiplay options" -background #d9d9d9 -height 165 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 150 
    set site_4_0 $site_3_0.lab49
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TCheckbutton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::checkbutton "$site_4_0.tCh52" \
        -variable "boundarybox_var" -text "Grain boundary box" -compound left 
    vTcl:DefineAlias "$site_4_0.tCh52" "CheckBox_BoundaryBox" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    bind $site_4_0.tCh52 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Draw a boundary box around each grain.}
    }
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TCheckbutton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::checkbutton "$site_4_0.tCh50" \
        -variable "numberedgrains_var" -text "Numbered grains" -compound left 
    vTcl:DefineAlias "$site_4_0.tCh50" "CheckBox_NumberedGrains" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    bind $site_4_0.tCh50 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Each grain recives a tag number}
    }
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TCheckbutton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::checkbutton "$site_4_0.tCh51" \
        -variable "minmax_var" -text "Hightlight min/max." -compound left 
    vTcl:DefineAlias "$site_4_0.tCh51" "CheckBox_minmax" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    bind $site_4_0.tCh51 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Highlight the smallest and the largest grains.}
    }
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TCheckbutton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::checkbutton "$site_4_0.tCh47" \
        -variable "drawcnt_var" -text "Draw contours" -compound left 
    vTcl:DefineAlias "$site_4_0.tCh47" "CheckBox" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TCheckbutton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::checkbutton "$site_4_0.tCh53" \
        -variable "colorfill_var" -text "Color fill grains" -compound left 
    vTcl:DefineAlias "$site_4_0.tCh53" "CheckBox_fill_grains" vTcl:WidgetProc "TopLevel_SegmentationWindow" 1
    bind $site_4_0.tCh53 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Fill grains interior}
    }
    place $site_4_0.tCh52 \
        -in $site_4_0 -x 10 -y 60 -anchor nw -bordermode ignore 
    place $site_4_0.tCh50 \
        -in $site_4_0 -x 10 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.tCh51 \
        -in $site_4_0 -x 10 -y 40 -anchor nw -bordermode ignore 
    place $site_4_0.tCh47 \
        -in $site_4_0 -x 10 -y 100 -anchor nw -bordermode ignore 
    place $site_4_0.tCh53 \
        -in $site_4_0 -x 10 -y 80 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 10 -y 20 -width 140 -relwidth 0 -height 175 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 160 -y 20 -width 170 -relwidth 0 -height 55 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 160 -y 80 -width 170 -relwidth 0 -height 55 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 160 -y 150 -width 87 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but48 \
        -in $site_3_0 -x 260 -y 150 -width 67 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 340 -y 20 -width 150 -relwidth 0 -height 165 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab47 \
        -in $top -x 10 -y 10 -width 500 -relwidth 0 -height 205 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top3 {base} {
    global vTcl
    if {$base == ""} {
        set base .top3
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #d9d9d9 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 329x92+964+338
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 845
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Image data"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "ImageDataWindow" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    labelframe "$top.lab53" \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -background #d9d9d9 -height 75 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -width 310 
    set site_3_0 $top.lab53
    label "$site_3_0.lab56" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Magnification                    X" 
    vTcl:DefineAlias "$site_3_0.lab56" "LabelMagnification" vTcl:WidgetProc "ImageDataWindow" 1
    label "$site_3_0.lab57" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Scale                   (um)" 
    vTcl:DefineAlias "$site_3_0.lab57" "LabelGetScale" vTcl:WidgetProc "ImageDataWindow" 1
    entry "$site_3_0.ent58" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #c4c4c4 \
        -selectforeground black -width 44 
    vTcl:DefineAlias "$site_3_0.ent58" "EntryMagnification" vTcl:WidgetProc "ImageDataWindow" 1
    entry "$site_3_0.ent59" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #c4c4c4 \
        -selectforeground black -width 44 
    vTcl:DefineAlias "$site_3_0.ent59" "EntryScale" vTcl:WidgetProc "ImageDataWindow" 1
    bind $site_3_0.ent59 <<SetBalloon>> {
        set ::vTcl::balloon::%W {After drawing a straight line over the image, type the value presented on the image.}
    }
    button "$site_3_0.but47" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -command "conclude_data_image_collect" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -pady 0 -text "OK" 
    vTcl:DefineAlias "$site_3_0.but47" "ButtonDataImageClose" vTcl:WidgetProc "ImageDataWindow" 1
    place $site_3_0.lab56 \
        -in $site_3_0 -x 10 -y 10 -anchor nw -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 60 -y 40 -anchor nw -bordermode ignore 
    place $site_3_0.ent58 \
        -in $site_3_0 -x 100 -y 10 -width 44 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent59 \
        -in $site_3_0 -x 100 -y 40 -width 44 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 200 -y 20 -width 77 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab53 \
        -in $top -x 10 -y 10 -width 310 -relwidth 0 -height 75 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top4 {base} {
    global vTcl
    if {$base == ""} {
        set base .top4
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #d9d9d9 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 440x311+963+465
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 845
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Grain Size - ASTM/E112-12"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "TopLevel_MeasuringProcedure" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    frame "$top.fra66" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 255 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 265 
    set site_3_0 $top.fra66
    label "$site_3_0.lab73" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Circle area" 
    label "$site_3_0.lab75" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Number of lines" 
    radiobutton "$site_3_0.rad54" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Jeffries - Planimetric procedure" -textvariable "Jeffries" \
        -value "1" -variable "RB_procedure" 
    vTcl:DefineAlias "$site_3_0.rad54" "RB_JeffriesP" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    label "$site_3_0.lab77" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Lines length" 
    label "$site_3_0.lab79" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Circle diameter" 
    entry "$site_3_0.ent74" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 34 
    vTcl:DefineAlias "$site_3_0.ent74" "CircunferenceJeffriesArea" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    entry "$site_3_0.ent76" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 34 
    vTcl:DefineAlias "$site_3_0.ent76" "NumLinesHeyns" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    entry "$site_3_0.ent78" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 34 
    vTcl:DefineAlias "$site_3_0.ent78" "LineLength" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    entry "$site_3_0.ent80" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 34 
    vTcl:DefineAlias "$site_3_0.ent80" "HilliardCircunferenceDiameterEntry" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    radiobutton "$site_3_0.rad55" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Heyns - Lineal Intercept procedure" -textvariable "Heyns" \
        -value "2" -variable "RB_procedure" 
    vTcl:DefineAlias "$site_3_0.rad55" "RB_HeynsP" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    bind $site_3_0.rad55 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Intercepting procedure}
    }
    radiobutton "$site_3_0.rad56" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Hilliard - Single circle" -value "3" -variable "RB_procedure" 
    vTcl:DefineAlias "$site_3_0.rad56" "RB_HilliardP" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    bind $site_3_0.rad56 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Intercepting procedure}
    }
    radiobutton "$site_3_0.rad62" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Abram - Three circles" -value "4" -variable "RB_procedure" 
    bind $site_3_0.rad62 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Intercepting procedure}
    }
    place $site_3_0.lab73 \
        -in $site_3_0 -x 30 -y 35 -anchor nw -bordermode ignore 
    place $site_3_0.lab75 \
        -in $site_3_0 -x 30 -y 95 -anchor nw -bordermode ignore 
    place $site_3_0.rad54 \
        -in $site_3_0 -x 10 -y 10 -anchor nw -bordermode ignore 
    place $site_3_0.lab77 \
        -in $site_3_0 -x 30 -y 120 -anchor nw -bordermode ignore 
    place $site_3_0.lab79 \
        -in $site_3_0 -x 40 -y 190 -anchor nw -bordermode ignore 
    place $site_3_0.ent74 \
        -in $site_3_0 -x 100 -y 35 -width 34 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent76 \
        -in $site_3_0 -x 130 -y 95 -width 34 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent78 \
        -in $site_3_0 -x 130 -y 120 -width 34 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent80 \
        -in $site_3_0 -x 130 -y 190 -width 34 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.rad55 \
        -in $site_3_0 -x 10 -y 70 -anchor nw -bordermode ignore 
    place $site_3_0.rad56 \
        -in $site_3_0 -x 10 -y 160 -anchor nw -bordermode ignore 
    place $site_3_0.rad62 \
        -in $site_3_0 -x 10 -y 220 -anchor nw -bordermode ignore 
    labelframe "$top.lab51" \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -text "Display options" -background #d9d9d9 -height 75 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 150 
    set site_3_0 $top.lab51
    checkbutton "$site_3_0.che52" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Bounding box" -variable "boundbox_var" 
    vTcl:DefineAlias "$site_3_0.che52" "BoundingBox_CheckBoxButton" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    bind $site_3_0.che52 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Displays a boundaing box around each grain}
    }
    checkbutton "$site_3_0.che53" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "Number grains" -variable "numbergrains_var" 
    vTcl:DefineAlias "$site_3_0.che53" "NumberGrains_CheckBoxButton" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    bind $site_3_0.che53 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Labels each grain used by the respective procedure}
    }
    place $site_3_0.che52 \
        -in $site_3_0 -x 10 -y 20 -anchor nw -bordermode ignore 
    place $site_3_0.che53 \
        -in $site_3_0 -x 10 -y 40 -anchor nw -bordermode ignore 
    button "$top.but57" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -command "apply_procedure_button" -compound left \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -pady 0 -text "Apply" 
    vTcl:DefineAlias "$top.but57" "ApplyProcudureButton" vTcl:WidgetProc "TopLevel_MeasuringProcedure" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra66 \
        -in $top -x 10 -y 10 -width 265 -relwidth 0 -height 255 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 280 -y 2 -anchor nw -bordermode ignore 
    place $top.but57 \
        -in $top -x 160 -y 270 -width 137 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
set btop2 ""
if {$vTcl(borrow)} {
    set btop2 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop2 $vTcl(tops)] != -1} {
        set btop2 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop2
Window show .top2 $btop2
if {$vTcl(borrow)} {
    $btop2 configure -background plum
}
set btop3 ""
if {$vTcl(borrow)} {
    set btop3 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop3 $vTcl(tops)] != -1} {
        set btop3 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop3
Window show .top3 $btop3
if {$vTcl(borrow)} {
    $btop3 configure -background plum
}
set btop4 ""
if {$vTcl(borrow)} {
    set btop4 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop4 $vTcl(tops)] != -1} {
        set btop4 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop4
Window show .top4 $btop4
if {$vTcl(borrow)} {
    $btop4 configure -background plum
}

