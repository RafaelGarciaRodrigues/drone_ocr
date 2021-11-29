<?php

 	if (isset($_POST['NomeArquivo'])) {
		$name = $_POST['NomeArquivo'];
		$text = $_POST['Conteudo'];
		$file = fopen($name, 'w+');
		fwrite($file, $text);
		fclose($file);
		ECHO " <<< POST RECEBIDO >>>";
	}
	
	$DADOS = "<DIV STYLE='display:none'>";
	$FORM = "<DIV STYLE='display:block'>";
	
	if (isset($_POST['TOKEN'])) {
		if ($_POST['TOKEN'] == '2105'){
			$DADOS = "<DIV STYLE='display:block'>";
			$FORM = "<DIV STYLE='display:none'>";
		}
	}
	
	if (isset($_POST['ALEXA'])) {
		if (isset($_POST['ArquivoAlexaServidor'])) {
			$name = $_POST['ArquivoAlexaServidor'].'.txt';
			$text = '{"result":"'.$_POST['Conteudo'].'"}';
			$file = fopen($name, 'w+');
			fwrite($file, $text);
			fclose($file);
			ECHO " <<< POST ALEXA RECEBIDO >>>";
		}
	}
?>


	
		<?php
			$FRAMES = "";
			$PAGINAS = 0;
			
			
			if(isset($_GET['p'])){
				$ATUAL_PAGE = $_GET['p'];
			}else{
				$ATUAL_PAGE = 0;
			}
						
			
			$pasta = getcwd();
			if(is_dir($pasta)){
				$diretorio = dir($pasta);
				$ID=0;
				while(($arquivo = $diretorio->read()) !== false){
					if (strpos($arquivo, '.html') > 0){
						$ID++;
						
						if($ID==$ATUAL_PAGE){
							$FRAMES .= "\n<DIV style='text-align: -webkit-center;'>\n	";
							$FRAMES .= "	<iframe src='".$arquivo."' title='' width='1000' height='650' scrolling='no' frameBorder='0' id='ID_".$ID."' onLoad=\"resizer('ID_".$ID."');\" marginheight='0'></iframe>\n		";
							$FRAMES .= "</DIV>\n	";
						}
						$PAGINAS++;
					}
				}
				$diretorio->close();
			}
		

			$PROXIMA_PAG = $ATUAL_PAGE + 1;
			if($PROXIMA_PAG > $PAGINAS){$PROXIMA_PAG=0;}
		
		?>


<HTML>
<HEAD>
	<TITLE>
		::: RELATÓRIO OPERACIONAL :::
	</TITLE>
	
	<?php
		header('Refresh: 15; URL=D_SLIDE_BASE.php?p='.$PROXIMA_PAG.'&PAGINAS='.$PAGINAS)
	?>




	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

	<script>
		function resizer(id)
		{
		var doc=document.getElementById(id).contentWindow.document;
		var body_ = doc.body, html_ = doc.documentElement;
		var height = Math.max( body_.scrollHeight, body_.offsetHeight, html_.clientHeight, html_.scrollHeight, html_.offsetHeight );
		var width  = Math.max( body_.scrollWidth, body_.offsetWidth, html_.clientWidth, html_.scrollWidth, html_.offsetWidth );
		document.getElementById(id).style.height=height;
		document.getElementById(id).style.width=width;
		}		
	</script>

</HEAD>
<BODY STYLE='background-color:#2a2a2a'>
	<DIV style="color: #FAF9F6;text-align-last: center;font-family: arial;font-size: 22;font-weight: bold;margin-bottom: 25;">
		RELATÓRIO OPERACIONAL
	</DIV>


	<?=$FRAMES?>



		
</BODY>
</HTML>