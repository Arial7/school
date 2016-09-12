#!/bin/zsh

function compile_specific() {
    local year=$1
    local class=$2
    local output_dir="$SCHOOL_DIR/renders/$year"

    if [ ! -d $output_dir ]; then
        mkdir -p output_dir
    fi

    local files=($SCHOOL_DIR/$year/$class/*)

    printf "Compiling class %s from year %s\n" $class $year

    pandoc -s -S --toc -c $SCHOOL_DIR/assets/style.css $files -t html5 -o "$output_dir/$class.html"
}

function compile_all() {
    local years=($(find $SCHOOL_DIR/* -maxdepth 0 -type d | grep -v "renders" | grep -v assets))

    for year in $years;
    do
        printf "Compiling year %s\n" $(basename $year)

        local classes=($(find $year/* -maxdepth 0 -type d))
        for class in $classes;
            printf "   - %s" $(basename $class)
            local files=($class/*)
            pandoc -s -S --toc -c $SCHOOL_DIR/assets/style.css $files -t html5 -o "$output_dir/$class.html"

    done
}

if [ -n "$1" ]; then
    compile_specific
else
    compile_all
fi
