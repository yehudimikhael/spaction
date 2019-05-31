var codeapp = angular.module('codeapp', ['nya.bootstrap.select', 
                                          'ngAnimate'
                                        ]);
                                    




                                        
codeapp.run(function($http){
    $http.defaults.headers.common.Authorization = 'Basic YmVlcDpib29w'
  });


codeapp.controller('homeController', function($scope, $http){

  $scope.popup = false;
  $scope.email = null;
  $scope.pass = null;
  $scope.pass2 = null;
  $scope.currentUser = null;
  $scope.check_pass = false;
  
  //Cadastro
  $scope.n_equipe = null;
  $scope.categoriaa = null;
  $scope.alergia_n = null;
  $scope.alergia_p = null;
  $scope.cnh = null;
  $scope.email = null;
  $scope.emergencia_p = null;
  $scope.emergencia_n = null;
  $scope.nome_navegador = null;
  $scope.nome_piloto = null;
  $scope.pl_saude_p = null;
  $scope.pl_saude_n = null;
  $scope.rg_navegador = null;
  $scope.t_sangue_p = null;
  $scope.t_sangue_p = null
  $scope.tel_p = null,
  $scope.tel_n = null
 






//Salvar Cadastro 
$scope.salvar = function(){
  var json_equipes = {}
  json_equipes["equipe"]= $scope.n_equipe,
  json_equipes["Categoria"]=$scope.categoriaa,
  json_equipes["alergia_n"]=$scope.alergia_n,
  json_equipes["alergia_p"]=$scope.alergia_p,
  json_equipes["cnh"]=$scope.cnh,
  json_equipes["email"]=$scope.email,
  json_equipes["emergencia_n"]=$scope.emergencia_n,
  json_equipes["emergencia_p"]=$scope.emergencia_p,
  json_equipes["nome_navegador"]=$scope.nome_navegador,
  json_equipes["nome_piloto"]=$scope.nome_piloto,
  json_equipes["pl_saude_n"]=$scope.pl_saude_n,
  json_equipes["pl_saude_p"]=$scope.pl_saude_p,
  json_equipes["rg_navegador"]=$scope.rg_navegador,
  json_equipes["t_sangue_n"]=$scope.t_sangue_n,
  json_equipes["t_sangue_p"]=$scope.t_sangue_p,
  json_equipes["tel_p"]=$scope.tel_p,
  json_equipes["tel_n"]=$scope.tel_n
  json_equipes["cidade"]=$scope.cidade
  json_equipes["veiculo"]=$scope.veiculo
 
  $http.post("https://app-login-6ea15.firebaseio.com/rallycarioca/equipes.json", json_equipes)
}

//Categoria
 $http({ 
   method: 'GET',
   url:'https://app-login-6ea15.firebaseio.com/rallycarioca/categoria.json',
   headers:{'X-Requested-With': 'XMLHttpRequest'},
    }).then(function sucessCallback(response){
      $scope.categoria = response.data;
      console.log($scope.categoria)
    });


//Tipo Sanguineo    
$http({ 
    method: 'GET',
    url:'https://app-login-6ea15.firebaseio.com/rallycarioca/t_sanguineo.json',
    headers:{'X-Requested-With': 'XMLHttpRequest'},
    }).then(function sucessCallback(response){
      $scope.sangue  = response.data;
      console.log($scope.categoria)
    });
    
//Classificação

$http({ 
  method: 'GET',
  url:'https://app-login-6ea15.firebaseio.com/rallycarioca/equipes.json',
  headers:{'X-Requested-With': 'XMLHttpRequest'},
  }).then(function sucessCallback(response){
    $scope.tb_equipes = []
    var teste = JSON.stringify(response.data)
    var id = Object.values(response.data)
    console.log(id.length)
    var i = 0;
    while(i < id.length){
      $scope.tb_equipes.push({
        categoria: id[i].Categoria,
        piloto: id[i].nome_piloto,
        navegador: id[i].nome_navegador,
        equipe: id[i].equipe,
        cidade: id[i].cidade,
        veiculo: id[i].veiculo
      })
      i++;
    }
  console.log($scope.tb_equipes)
  });

 $scope.t_tables = [
          {
            "name" : "GRADUADO"},
          {
            "name" : "PILOTO"},
          {
            "name" : "NAVEGADOR"},
          {
            "name" : "EQUIPE"},
          {
            "name" : "CIDADE"},
          {
            "name" : "VEÍCULO"}
   ]



  //Poppup
  $scope.change= function(){
    if($scope.popup == false){
      $scope.popup = true;
      //console.log($scope.popup)
    }
    else{
      $scope.popup = false;
      //console.log($scope.popup)
    }
    
  }
  
  //Login Firebase
  var config = {
    apiKey: "AIzaSyB0d7KpX5qBdjByP98zH59sUKZY7qrjXJc",
    authDomain: "app-login-6ea15.firebaseapp.com",
    databaseURL: "https://app-login-6ea15.firebaseio.com",
    storageBucket: "app-login-6ea15.appspot.com",
    messagingSenderId: "909869376531",
  };
  firebase.initializeApp(config)

  // //Verificar se está logado ou não
  // $scope.check_login = function(){
  //   var user = $scope.email;
  //   firebase.auth().onAuthStateChanged(function(user){
  //     if(user){
  //       console.log("Logado")
  //     }else{
  //       $scope.loging_firebase()
  //     }

  //   })
  // }
  //$scope.check_login()

//Fazer Login
  $scope.loging_firebase = function(){
    firebase.auth().signInWithEmailAndPassword($scope.email, $scope.pass)
    .then(function(firebaseUser){
      $scope.currentUser = firebaseUser.email;
      $scope.change();
      
    })    
    .catch(function(error){
      var errorCode = error.code;
      var errorMEssage = error.message;
      if (errorCode === 'auth/wrong-password') {
        alert('Usuário/Senha incorreto');
        
      } else {
        alert(errorMessage);
        
      }
      console.log(error);
      
    });
    
  }

  //Cadastro Novo Usuario
  $scope.cadastro = function(){
    var email = $scope.email
    var pass = $scope.pass
    if($scope.pass == $scope.pass2){
      $scope.check_pass = false;
    firebase.auth().createUserWithEmailAndPassword(email, pass)
    .then(function(){
      console.log("Usuario Cadastrado ");
    })
    .catch(function(error){
      console.log(error);
    });
    }
    else {
      $scope.check_pass = true;
    }
  }







  //Logout
  // $scope.logout = function(){
  //   firebase.auth().signOut()
  //   .then(function(){
  //     $scope.currentUser = null;
  //     //$scope.popup = 1;        
  //     console.log("Logout")
  //   }, function(error){
  //     console.log(error)
  //   })
  // }

  //Alterar Senhar
  // $scope.change_password = function(){
  //   var pass = "Valor da nova senha"
  //   firebase.auth().currentUser.updatePassword(pass)
  //   .then(function(){ console.log("Senha Alterada")}
  //   .catch(function(error){ console.log(error)}))    
  // }


});