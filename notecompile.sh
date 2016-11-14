#!/bin/zsh

function compile_specific() {
    local class=$1
    local output_dir="$SCHOOL_DIR/renders/"

    if [ ! -d $output_dir ]; then
        mkdir -p output_dir
    fi

    local files=($SCHOOL_DIR/$class/*(.))

    if [ -n "$files" ]; then
        printf "Compiling class %s \n" $class
        pandoc -s -S --toc -c $SCHOOL_DIR/assets/style.css $files -f markdown -t html5 -o "$output_dir/$class.html"
    else
        printf "No files for %s \n" $class
    fi

}

function compile_all() {
    local classes=($(find $SCHOOL_DIR/* -maxdepth 0 -type d | grep -v "renders" | grep -v "assets"))

    for classpath in $classes;
    do
        printf "Current folder: %s \n" $classpath
        local class=$(basename $classpath)
        compile_specific $class
    done
}

if [ -n "$1" ]; then
    compile_specific
else
    compile_all
fi
