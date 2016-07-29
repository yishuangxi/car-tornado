/**
 * Created by yishuangxi on 16/7/29.
 */

var gulp = require('gulp')
var gulp_file_include = require('gulp-file-include')
var gulp_htmlmin = require('gulp-htmlmin')

//html文件include合并, 压缩
gulp.task('html', function () {
    return gulp.src('./template-src/**/*')
        .pipe(gulp_file_include({
            prefix: '@@',
            basepath: '@file'
        }))
        .pipe(gulp_htmlmin({collapseWhitespace: true}))
        .pipe(gulp.dest('./template'))
})


