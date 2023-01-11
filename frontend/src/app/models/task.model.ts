export interface Task {
  id: number;
  name: string;
  details: string;
  status: number;
  priority: number;
  creation_date: Date;
  alteration_date: Date;
  project_id: number;
}
