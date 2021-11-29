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

<HTML>
<HEAD>
	<TITLE>
		::: RELATÓRIO OPERACIONAL :::
	</TITLE>
	<meta http-equiv="refresh" content="60">
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
	<?=$FORM?>
		<DIV style="text-align: -webkit-center;">
			<form method="POST" style="width: 200px;">
			  <div class="form-group">
				<label for="exampleInputEmail1">TOKEN</label>
				<input type="tel" class="form-control" id="TOKEN" name="TOKEN" aria-describedby="TOKEN" placeholder="TOKEN">
				<small id="emailHelp" class="form-text text-muted">Informe o Token para acessar os dados.</small>
			  </div>
			  <button type="submit" class="btn btn-primary">Enviar</button>
			</form>	
		</DIV>
	</DIV>
	<?=$DADOS?>
		<?php
			$pasta = getcwd();
			if(is_dir($pasta)){
				$diretorio = dir($pasta);
				$ID=0;
				while(($arquivo = $diretorio->read()) !== false){
					if (strpos($arquivo, '.html') > 0){
						$ID++;
						echo "\n<DIV style='text-align: -webkit-center;'>\n	";
						echo "	<iframe src='".$arquivo."' title='' width='1000' height='650' scrolling='no' frameBorder='0' id='ID_".$ID."' onLoad=\"resizer('ID_".$ID."');\" marginheight='0'></iframe>\n		";
						echo "</DIV>\n	";
					}
				}
				$diretorio->close();
			}
		?>
	</DIV>	
</BODY>
</HTML>