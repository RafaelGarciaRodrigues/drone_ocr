<?php
 
	if (isset($_POST['NomeArquivo'])) {
		$name = $_POST['NomeArquivo'].'.txt';
		$text = '{"result":"'.$_POST['Conteudo'].'"}';
		$file = fopen($name, 'w+');
		fwrite($file, $text);
		fclose($file);
	}
?>


<html>
	<head>
	</head>
	<body>
		<form method="post">
	  
			<TABLE>
				<TR>
					<TD>
						<input type="text" id="NomeArquivo" name="NomeArquivo">
					</TD>
				</TR>
				<TR>
					<TD>
						<textarea  id="Conteudo" name="Conteudo"></textarea>
					</TD>
				</TR>
				<TR>
					<TD>
						<button>Enviar</button>
					</TD>
				</TR>				
			</TABLE>
		</form>
	</body>
</html>