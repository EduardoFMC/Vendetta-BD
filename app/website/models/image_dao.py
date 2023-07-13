class Image:
    def __init__(self, image_id, data, file_name, mime_type, created_at):
        self.image_id = image_id
        self.data = data
        self.file_name = file_name
        self.mime_type = mime_type
        self.created_at = created_at

class ImageDAO:
    def __init__(self):
        pass

    def get_all(self, cursor):
        try:
            sql_command = "SELECT * FROM Image"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            images = [Image(*image) for image in result]
            return images
        
        except Exception as e:
            print(e)
            return None
    
    def find_by_id(self, cursor, image_id):
        try:
            sql_command = "SELECT * FROM Image WHERE image_id = {}".format(str(image_id))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            image = Image(*result)
            return image
        
        except Exception as e:
            print(e)
            return None
    
    def add(self, cursor, image):
        try:
            sql_command = "INSERT INTO Image (data, file_name, mime_type) VALUES (%(data)s, %(file_name)s, %(mime_type)s)"
            data_insert = {"data": image.data, "file_name": image.file_name, "mime_type": image.mime_type}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)
    
    # NEcessário?
    def update():
        pass

    def delete(self, cursor, image_id):
        try:
            sql_command = "DELETE FROM Image WHERE image_id = {}".format(str(image_id))
            cursor.execute(sql_command)
            
        except Exception as e:
            print(e)