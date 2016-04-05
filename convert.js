// Generated by CoffeeScript 1.10.0
(function() {
  var Log, RENDERED_FILES_DIR, SCHOOL_FILES_DIR, clarguments, fs, homedir, log, markdownpdf, path, render, resolvePath;

  markdownpdf = require("markdown-pdf");

  fs = require("fs");

  clarguments = require("command-line-args");

  path = require("path");

  homedir = require("homedir");

  Log = require("loggos");

  log = new Log();

  SCHOOL_FILES_DIR = path.resolve(homedir(), "school/");

  RENDERED_FILES_DIR = path.resolve(homedir(), "school/renders/");

  resolvePath = function(file) {
    var filename, newExt, relativePathToBase;
    filename = "/" + path.basename(file, ".md");
    relativePathToBase = "/" + path.dirname(path.relative(SCHOOL_FILES_DIR, file));
    newExt = ".pdf";
    return path.resolve(RENDERED_FILES_DIR + relativePathToBase + filename + ".pdf");
  };

  render = function(inputs) {
    if (typeof inputs === Array) {
      log.info("Convert", "Rendering " + inputs.length + " files");
    } else {
      log.info("Convert", "Rendering " + inputs);
    }
    return markdownpdf().from(inputs).to(resolvePath(inputs), function() {
      return log.info("Convert", "Done");
    });
  };

  render(process.argv[2]);

}).call(this);