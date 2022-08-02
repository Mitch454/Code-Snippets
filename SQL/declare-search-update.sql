DECLARE @search AS VARCHAR(100)
SET @search = 'Z:\Steve Williams\'


 UPDATE tblJobAttachment
 SET Attachment = 'Z:\Steve Williams\' + RIGHT(Attachment, (len(Attachment) - 18))
 WHERE LEFT(Attachment, 18) = @search


