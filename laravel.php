creat Project:
#putt name of the project in place of blog
composer create-project --prefer-dist laravel/laravel blog   



#creat a virtual host for you project
https://www.cloudways.com/blog/configure-virtual-host-on-windows-10-for-wordpress/

#making auth
#5.2
php artisan make:auth
#6
composer require laravel/ui
php artisan ui vue --auth


#make middleware
https://laracasts.com/discuss/channels/general-discussion/create-middleware-to-auth-admin-users?page=0

#Add this to admin 
use Illuminate\Support\Facades\Auth;

#add this to routing file 
Route::group(['prefix' => 'backend'], function () {
    Auth::routes();
});

Route::group(['prefix' => 'backend', 'middleware' => 'admin'], function () {
    Route::get('admin-dashboard', 'Backend/AdminController@dashboard');
});



php artisan make:controller SiteController  // making controller


after git,
composer update
mv .env.example .env
genrate key artasian
