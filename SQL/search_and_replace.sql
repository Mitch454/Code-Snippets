DECLARE @search AS VARCHAR(100)
SET @search = 'StringToSearch'


 UPDATE tblJobAttachment
 SET Attachment = 'StringToReplaceWith' + RIGHT(Attachment, (len(Attachment) - 14))
 WHERE LEFT(Attachment, 14) = @search


