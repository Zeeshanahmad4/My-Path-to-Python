creat Project:
#putt name of the project in place of blog
composer create-project --prefer-dist laravel/laravel blog   





                                        #Routes
https://laravel.com/docs/5.2/routing#route-parameters
https://laravel.com/docs/5.2/routing#named-routes


                                        #Controller
https://laravel.com/docs/5.2/controllers#basic-controllers
https://laravel.com/docs/5.2/controllers#restful-resource-controllers
route::resource('posts','PostController');

                                        #views

sending data through view
route::get('pass/{name}/{id}/{pass}','PostController@zee');
blade {{$name}} {{$id}} {{$pass}}
    public function zee($name,$id,$pass){

        return view('passdata',compact ('name','id', 'pass'));

    }




#creat a virtual host for you project

https://www.cloudways.com/blog/configure-virtual-host-on-windows-10-for-wordpress/

#making auth
#5.2
php artisan make:auth
#6
composer require laravel/ui
php artisan ui vue --auth
npm install && npm run dev


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


#seeder
php artisan make:migration create_users_table
Set schema and foriegn key
php artisan make migration
php artisan migrate


php artisan make:controller SiteController  // making controller


#admin panel
quickadmin

#DATABASE 
php artisan 
php artisan db:seed
after git,
composer update
mv .env.example .env
genrate key artasian
