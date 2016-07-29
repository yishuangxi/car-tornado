/**
 * Created by yishuangxi on 16/7/29.
 */

var gulp = require('gulp')
var gulp_file_include = require('gulp-file-include')

gulp.task('include', function () {
    gulp.src('./template-src/**/*')
        .pipe(gulp_file_include({
            prefix: '@@',
            basepath: '@file'
        }))
        .pipe(gulp.dest('./template'))
})