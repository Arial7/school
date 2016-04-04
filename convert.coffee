markdownpdf = require "markdown-pdf"
fs          = require "fs"
clarguments = require "command-line-args"
path        = require "path"
homedir     = require "homedir"
Log         = require "loggos"
log         = new Log()

SCHOOL_FILES_DIR = path.resolve homedir(), "school/"
RENDERED_FILES_DIR = path.resolve homedir(), "school/renders/"

# Resolve the path from the note file to the rendered files dir
resolvePath = (file) ->
    filename = "/" + path.basename file, ".md"
    # i.e. 12-2/ethik/
    relativePathToBase = "/" + path.dirname path.relative SCHOOL_FILES_DIR, file
    newExt = ".pdf"

    path.resolve RENDERED_FILES_DIR + relativePathToBase + filename + ".pdf"

render = (inputs) ->
    if typeof inputs is Array
        log.info "Convert", "Rendering #{inputs.length} files"
    else
        log.info "Convert", "Rendering #{inputs}"
    
   

   
    markdownpdf().from(inputs)
        .to(resolvePath(inputs), ->
            log.info "Convert", "Done")

render process.argv[2]
