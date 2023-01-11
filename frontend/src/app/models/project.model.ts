export interface Project {
  id: number;
  name: string;
  details: string;
  status: number;
  creation_date: Date;
  alteration_date: Date;
  task_id: number[];
}
